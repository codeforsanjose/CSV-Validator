# validate_columns takes a string input which is the path/filename
# to the file to validate as CKAN ready. Raises CkanError exceptions:
# DuplicateColumnError in the event that one or more column name is duplicated,
# ColumnMismatchError in the event that not all rows in the file
# have the same number of columns, NoDataError if the file contains
# only a single column or row.

# Created November 2016 by Lisa Litchfield.


import os.path
import csv, sys
from collections import defaultdict
class CkanError(Exception):pass
class DuplicateColumnError(CkanError):pass
class NoDataError(CkanError):pass
class ColumnMismatchError(CkanError):
    def __str__(self):
        return 'Not all rows have the same number of columns!'
def validate_columns(input_file):

    frequencies = defaultdict(int)
    duplicates = []
    headers = set()
    if not os.path.isfile(input_file):
        print("Filepath {} is invalid".format(input_file))
        return
      
    # open with universal newline mode enabled to prevent csv.Error: new-line character seen in unquoted field
    with open(input_file, 'rU') as csvfile:
        file_reader = csv.reader(csvfile)
        # check for duplicate column names
        first_line = file_reader.next()
        for column_name in first_line:
            if column_name in headers:
                duplicates.append(column_name)
                continue
            headers.add(column_name)

        column_count = len(headers)
        if column_count <2:
            raise NoDataError("Data file contains fewer than 2 columns!")
        if len(duplicates) > 0:
            raise DuplicateColumnError(
                'duplicate column names: {}'.format(
                    ', '.join(duplicates)
                )
            )
        # check for proper number of columns in every row
        row_count = 0
        for row in file_reader:
            row_count += 1
            if len(row) != column_count:
                raise ColumnMismatchError
        if row_count < 1:
            raise NoDataError("Data file contains fewer than 2 rows!")

        
if __name__ == '__main__':
    if len(sys.argv) is 1:
        print("no arguments provided; running the program "
              "against some sample CSV files")
        validate_columns("test_files/valid.csv")
        validate_columns("test_files/rowLengthMismatch.csv")
        validate_columns("test_files/tooFewColumns.csv")
    else:
        for arg in sys.argv[1:]:
            validate_columns(arg)
