# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

s1 = b'attribute'
# s2 = b'класс' - не отображается, потому, что кириллица, не ASCII
# s3 = b'функция' - не отображается, потому, что кириллица, не ASCII
s4 = b'type'

print(s4)