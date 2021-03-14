# Программа сервера для отправки приветствия сервера и получения ответа
from socket import *


def data_client():
    s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    s.connect(("localhost", 8007))  # Соединиться с сервером
    msg = "Hi server!"
    s.send(msg.encode("ascii"))
    data = s.recv(1000000)
    print("Сообщение от сервера: ", data.decode("ascii"), ", длиной ", len(data), " байт")
    s.close()
    return {"Сообщение от сервера: ": data.decode("ascii"), ", длиной ": [len(data), " байт"]}


data_client()
