# Программа клиента, запрашивающего текущее время
from socket import *
def time_client():
    s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    s.connect(('localhost', 8888))  # Соединиться с сервером
    tm = s.recv(1024)  # Принять не более 1024 байтов данных
    s.close()
    return tm.decode('ascii')
# print("Текущее время: %s" % time_client())