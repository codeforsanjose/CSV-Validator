import unittest
import sys

from validate import validate_columns
from validate import NoDataError
from validate import ColumnMismatchError
from validate import DuplicateColumnError


class TestCSVValidator(unittest.TestCase):

    def test_row_lengths(self):
        with self.assertRaises(NoDataError):
            validate_columns('test_files/tooFewColumns.csv')

    def test_duplicated_column_names(self):
        with self.assertRaises(DuplicateColumnError):
            validate_columns('test_files/duplicatedColumnNames.csv')

    def test_row_length_mismatch(self):
        with self.assertRaises(ColumnMismatchError):
            validate_columns('test_files/rowLengthMismatch.csv')

    def test_validate_columns_invalid_file(self):
        r = validate_columns('/this/better/not/exist/on/your/system')
        assert r is None


if __name__ == '__main__':
    unittest.main()
