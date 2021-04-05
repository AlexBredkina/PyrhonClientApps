# Программа сервера для отправки приветствия сервера и получения ответа
from socket import *
import json
import logging
import select
import log.client_log_config
import sys

logger = logging.getLogger('CLIENT')
ENCODING = "utf-8"

# with socket(AF_INET, SOCK_STREAM) as s:  # Создать сокет TCP
#     try:
#         s.connect(("localhost", 8007))  # Соединиться с сервером
#     except ConnectionRefusedError as NoConnection:
#         logger.error(NoConnection)
#     auth = {
#         "action": "authenticate",
#         "time": 123,
#         "user": {
#             "account_name": "C0deMaver1ck",
#             "password": "CorrectHorseBatteryStaple"
#         }
#     }
#
#     msg = json.dumps(auth)
#     s.send(msg.encode(ENCODING))
#     data = s.recv(1000000)
#     recv_str = data.decode(ENCODING)
#     print("Сообщение от сервера: ", recv_str, ", длиной ", len(data), " байт")
#     a = f'"Сообщение от сервера: ", {recv_str}, ", длиной ", {len(data)}, " байт"'
#     logger.info(a)
#     recv_msg = json.loads(recv_str)


ADDRESS = ('localhost', 10000)


def echo_client():
    # Начиная с Python 3.2 сокеты имеют протокол менеджера контекста
    # При выходе из оператора with сокет будет автоматически закрыт
    with socket(AF_INET, SOCK_STREAM) as sock:  # Создать сокет TCP
        sock.connect(ADDRESS)  # Соединиться с сервером
        while True:
            # msg = input('Ваше сообщение: ')
            # if msg == 'exit':
            #     break
            # если я верно поняла то мы просто пилим сюда готовое сообщение
            auth = {"action": "msg",
                    "time": "123",
                    "from": "account_name",
                    "encoding": "utf-8",
                    "message": "message"
                    }
            msg = str(auth)

            sock.send(msg.encode(ENCODING))
            data = sock.recv(1024).decode(ENCODING)
            logger.info('Ответ:', data)


if __name__ == '__main__':
    echo_client()
