from HW4.data_client import data_client
import unittest


class TestClient(unittest.TestCase):
    def test_message(self):
        msg = data_client()
        greeting = msg["Сообщение от сервера: "]
        self.assertEqual(greeting, "Hi client!")


if __name__ == '__main__':
    unittest.main()
