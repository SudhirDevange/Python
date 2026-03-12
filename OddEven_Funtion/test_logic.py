import unittest
from logic import check_odd_even

class TestOddEven(unittest.TestCase):
    def test_even_number(self):
        self.assertEqual(check_odd_even(4), "Even")

    def test_odd_number(self):
        self.assertEqual(check_odd_even(7), "Even")

    def test_invalid_input(self):
        self.assertIsNone(check_odd_even("abc"))

if __name__ == '__main__':
    unittest.main()
