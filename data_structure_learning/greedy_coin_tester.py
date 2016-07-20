import unittest
from greedy_coin_counting import *

class CoinTest(unittest.TestCase):
    def test_greedy(self):
        s = money_counter(1)
        self.assertEqual(s.find("1\n"), 47)
        s = money_counter(19)
        self.assertEqual(s.find("1\n"), 11)
        self.assertEqual(s.find("5 bills: 1\n"), 14)
        self.assertEqual(s.find("2\n"), 35)

if __name__ == "__main__":
    unittest.main()
