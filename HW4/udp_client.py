# Программа клиента, передающего серверу сообщения при каждом запросе на соединение
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:
    s.sendto("Запрос на соединение!".encode("utf-8"), ("127.0.0.1", 8888))
