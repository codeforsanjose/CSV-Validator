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

    def test_validate_columns_invalid_file(self):
        r = validate_columns('/this/better/not/exist/on/your/system')
        assert r is None

    def test_validate_columns_duplicate_columns(self):
        with self.assertRaises(DuplicateColumnError):
            validate_columns('test_files/duplicate_columns.csv')


if __name__ == '__main__':
    unittest.main()
