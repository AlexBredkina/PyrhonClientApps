import unittest
from HW4.udp_server import serv

class MyTestCase(unittest.TestCase):
    def test_something(self):
        msg = "Запрос на соединение!".encode("utf-8")
        self.assertEqual(serv(), msg)


if __name__ == '__main__':
    unittest.main()
