import unittest
import sys

from validate import validate_columns

class TestCSVValidator(unittest.TestCase):

    def test_empty_arg(self):
        with self.assertRaises(IOError):
            validate_columns('')

	def test_row_lengths(self):
		with self.assertRaises(ValueError):
			validate_columns('test_files/tooFewColumns.csv')


if __name__ == '__main__':
    unittest.main()