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

    def test_duplicated_column_names(self):
        with self.assertRaises(ValueError):
            validate_columns('test_files/duplicatedColumnNames.csv')

    def test_row_length_mismatch(self):
        with self.assertRaises(ValueError):
            validate_columns('test_files/rowLengthMismatch.csv')

if __name__ == '__main__':
    unittest.main()