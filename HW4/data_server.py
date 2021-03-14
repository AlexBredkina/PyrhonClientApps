# Программа сервера для получения приветствия от клиента и отправки ответа
from contextlib import closing
from socket import *


def data_server():
    with socket(AF_INET, SOCK_STREAM) as s:  # Создает сокет TCP
        s.bind(("", 8007))  # Присваивает порт 8007
        s.listen()

        while True:
            client, addr = s.accept()
            with closing(client) as cl:
                data = cl.recv(1000000)
                print(
                    "Сообщение: ",
                    data.decode("ascii"),
                    ", было отправлено клиентом: ",
                    addr,
                )

                msg = "Hi client!"
                cl.send(msg.encode("ascii"))
                return {
                    "Сообщение: ":
                        data.decode("ascii"),
                    ", было отправлено клиентом: ":
                        addr}


data_server()
