import unittest
from third import count_letter_in_string

class test_count_letter_in_string(unittest.TestCase):

    def test_count_letter_in_string_valid_input(self):
        self.assertEqual(count_letter_in_string('kacsa', 'a'), 2)

    def test_count_letter_in_string_not_contained(self):
        self.assertEqual(count_letter_in_string('majom', 'k'), 0)

    def test_count_letter_in_string_invalid_input_type(self):
        self.assertEqual(count_letter_in_string([1, 2, 3, 2], '2'), 0)

if __name__ == '__main__':
    unittest.main()
