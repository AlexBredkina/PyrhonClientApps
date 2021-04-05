# Программа сервера для получения приветствия от клиента и отправки ответа
import select
from contextlib import closing
from socket import socket, AF_INET, SOCK_STREAM
import json
import logging
import log.server_log_config

logger = logging.getLogger('SERVER')

ENCODING = "utf-8"


# with socket(AF_INET, SOCK_STREAM) as s:  # Создает сокет TCP
#     s.bind(("", 8007))  # Присваивает порт 8007
#     s.listen()
#
#     while True:
#         client, addr = s.accept()
#         with closing(client) as cl:
#             while True:
#                 data = cl.recv(1000000)
#                 recv_str = data.decode(ENCODING)
#                 print(
#                     "Сообщение: ",
#                     recv_str,
#                     ", было отправлено клиентом: ",
#                     addr,
#                 )
#                 a = f'"Сообщение : ", {recv_str}, ", было отправлено клиентом: ", {addr}'
#                 logger.info(a)
#                 print(a)
#
#                 recv_msg = json.loads(recv_str)
#                 if "action" in recv_msg and recv_msg["action"] == "authenticate":
#                     msg = {
#                         "response": 200,
#                         "alert": "Необязательное сообщение/уведомление"
#                     }
#                     msg = json.dumps(msg)
#                     cl.send(msg.encode(ENCODING))


def read_requests(r_clients, all_clients):
    """ Чтение запросов из списка клиентов
   """
    responses = {}  # Словарь ответов сервера вида {сокет: запрос}

    for sock in r_clients:
        try:
            data = sock.recv(1024).decode('utf-8')
            responses[sock] = data
        except:
            logger.info('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)

    return responses


def write_responses(requests, w_clients, all_clients):
    """ Эхо-ответ сервера клиентам, от которых были запросы
   """

    for sock in w_clients:
        try:
            resp = requests[sock].encode(ENCODING)
            # Подготовить и отправить ответ сервера
            sock.send(resp.upper())
            # Эхо-ответ сделаем чуть непохожим на оригинал

        except:

            logger.info('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            sock.close()
            all_clients.remove(sock)


def mainloop():
    """ Основной цикл обработки запросов клиентов
   """
    address = ('', 10000)
    clients = []

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    s.settimeout(0.2)  # Таймаут для операций с сокетом
    while True:
        try:
            conn, addr = s.accept()  # Проверка подключений
        except OSError as e:
            pass  # timeout вышел
        else:
            logger.info("Получен запрос на соединение от %s" % str(addr))
            clients.append(conn)
        finally:
            # Проверить наличие событий ввода-вывода
            wait = 10
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass  # Ничего не делать, если какой-то клиент отключился

            requests = read_requests(r, clients)  # Сохраним запросы клиентов
            if requests:
                write_responses(requests, w, clients)  # Выполним отправку ответов клиентам


logger.info('Эхо-сервер запущен!')
mainloop()
