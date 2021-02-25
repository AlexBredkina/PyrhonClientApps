# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать
# результаты из байтовового в строковый тип на кириллице.

import subprocess

args = ['ping', 'yandex.ru']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    # выводим результат в байтах
    print(line)

    # изменяем кодировку результата
    line = line.decode('cp866').encode('utf-8')
    # выводи результат в кодировке utf-8
    print(line.decode('utf-8'))

args2 = ['ping', 'youtube.com']
subproc_ping2 = subprocess.Popen(args2, stdout=subprocess.PIPE)
for line in subproc_ping2.stdout:
    # выводим результат в байтах
    print(line)

    # изменяем кодировку результата
    line = line.decode('cp866').encode('utf-8')
    # выводи результат в кодировке utf-8
    print(line.decode('utf-8'))
