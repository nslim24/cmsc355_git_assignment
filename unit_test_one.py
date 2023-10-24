import time_prog
import unittest

class testTime(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(time_prog.hours(210), 3.5)

if __name__ == '__main__':
    unittest.main