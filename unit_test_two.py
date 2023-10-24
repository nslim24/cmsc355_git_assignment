import time_prog
import unittest

class testTime(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(time_prog.hours(240), 4.5)

if __name__ == '__main__':
    unittest.main