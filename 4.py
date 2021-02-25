# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
# в байтовое и выполнить обратное преобразование (используя методы encode и decode).


#  строковые
a = 'разработка'
b = 'администрирование'
c = 'protocol'
d = 'standard'

# байтовые
a_bytes = a.encode('utf-8')
b_bytes = b.encode('utf-8')
c_bytes = c.encode('utf-8')
d_bytes = d.encode('utf-8')
print(a_bytes)
# вывело слово разработка в utf-8

# обратно в строку

a_back = a_bytes.decode('utf-8')
b_back = b_bytes.decode('utf-8')
c_back = c_bytes.decode('utf-8')
d_back = d_bytes.decode('utf-8')

print(a_back)
# вывело слово разработка