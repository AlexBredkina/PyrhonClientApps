from HW4.time_client import time_client
import time
import unittest
import pytest


class TestTime(unittest.TestCase):
    def test_time(self):
        self.assertEqual(
            time_client(), time.ctime(time.time())
        )


if __name__ == '__main__':
    unittest.main()
