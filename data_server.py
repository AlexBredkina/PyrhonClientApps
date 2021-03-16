# Программа сервера для получения приветствия от клиента и отправки ответа
from contextlib import closing
from socket import *
import json
import logging
import log.server_log_config

logger = logging.getLogger('SERVER')



ENCODING = "utf-8"

with socket(AF_INET, SOCK_STREAM) as s:  # Создает сокет TCP
    s.bind(("", 8007))  # Присваивает порт 8007
    s.listen()

    while True:
        client, addr = s.accept()
        with closing(client) as cl:
            while True:
                data = cl.recv(1000000)
                recv_str = data.decode(ENCODING)
                print(
                    "Сообщение: ",
                    recv_str,
                    ", было отправлено клиентом: ",
                    addr,
                )
                a = f'"Сообщение : ", {recv_str}, ", было отправлено клиентом: ", {addr}'
                logger.info(a)
                print(a)

                recv_msg = json.loads(recv_str)
                if "action" in recv_msg and recv_msg["action"] == "authenticate":
                    msg = {
                        "response": 200,
                        "alert": "Необязательное сообщение/уведомление"
                    }
                    msg = json.dumps(msg)
                    cl.send(msg.encode(ENCODING))