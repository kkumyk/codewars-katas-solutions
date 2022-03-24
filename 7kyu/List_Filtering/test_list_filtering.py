import unittest
from list_filtering import filter_list

class TestListFiltering(unittest.TestCase):
    def test_should_return_1_2(self):
        expected = [1, 2]
        actual = filter_list([1, 2, 'a', 'b', 9.2])

        self.assertEqual(expected, actual)


    def test_should_return_1_0_15(self):
        expected = [1, 0, 15]
        actual = filter_list([1, 'a', 'b', 0, 15])
        self.assertEqual(expected, actual)


    def test_should_return_1_2_123(self):
        expected = [1, 2, 123]
        actual = filter_list([1, 2, 'aasf', '1', '123', 123])
        self.assertEqual(expected, actual)