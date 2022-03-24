import unittest
from very_even_numbers import is_very_even_number

class TestVeryEvenNumbers(unittest.TestCase):
    def test_should_return_true(self):
        expected = True
        actual = is_very_even_number(848)
        self.assertEqual(expected, actual)


    def test_should_return_false(self):
        expected = False
        actual = is_very_even_number(12)
        self.assertEqual(expected, actual)
