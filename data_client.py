# Программа сервера для отправки приветствия сервера и получения ответа
from socket import *
import json


ENCODING = "utf-8"

with socket(AF_INET, SOCK_STREAM) as s:# Создать сокет TCP
    s.connect(("localhost", 8007))  # Соединиться с сервером

    auth = {
        "action": "authenticate",
        "time": 123,
        "user": {
                "account_name":  "C0deMaver1ck",
                "password":      "CorrectHorseBatteryStaple"
        }
    }

    msg = json.dumps(auth)
    s.send(msg.encode(ENCODING))
    data = s.recv(1000000)
    recv_str = data.decode(ENCODING)
    print("Сообщение от сервера: ", recv_str, ", длиной ", len(data), " байт")
    recv_msg = json.loads(recv_str)
