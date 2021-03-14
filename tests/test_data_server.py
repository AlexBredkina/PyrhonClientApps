from HW4.data_server import data_server

import unittest

# не прошло.   s.bind(("", 8007))  # Присваивает порт 8007
# OSError: [WinError 10048] Обычно разрешается только одно использование адреса сокета (протокол/сетевой адрес/порт)
# нужна подсказка (((

class TestClient(unittest.TestCase):
    def test_message(self):
        msg = data_server()
        greeting = msg["Сообщение: "]
        self.assertEqual(greeting, "Hi server!")


if __name__ == '__main__':
    unittest.main()