# Программа сервера для отправки приветствия сервера и получения ответа
from socket import *
import json
import logging
import log.client_log_config

logger = logging.getLogger('CLIENT')
ENCODING = "utf-8"

with socket(AF_INET, SOCK_STREAM) as s:  # Создать сокет TCP
    try:
        s.connect(("localhost", 8007))  # Соединиться с сервером
    except ConnectionRefusedError as NoConnection:
        logger.error(NoConnection)
    auth = {
        "action": "authenticate",
        "time": 123,
        "user": {
            "account_name": "C0deMaver1ck",
            "password": "CorrectHorseBatteryStaple"
        }
    }

    msg = json.dumps(auth)
    s.send(msg.encode(ENCODING))
    data = s.recv(1000000)
    recv_str = data.decode(ENCODING)
    print("Сообщение от сервера: ", recv_str, ", длиной ", len(data), " байт")
    a = f'"Сообщение от сервера: ", {recv_str}, ", длиной ", {len(data)}, " байт"'
    logger.info(a)
    recv_msg = json.loads(recv_str)
