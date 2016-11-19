# validate_columns takes a string input which is the path/filename to the file to validate as CKAN ready.
# Raises CkanError exceptions: DuplicateColumnError in the event that one or more column name is duplicated,
# ColumnMismatchError in the event that not all rows in the file have the same number of columns,
# NoDataError if the file contains only a single column or row.
# Created November 2016 by Lisa Litchfield.

import csv
from collections import defaultdict
class CkanError(Exception):pass
class DuplicateColumnError(CkanError):pass
class NoDataError(CkanError):pass
class ColumnMismatchError(CkanError):
    def __str__(self):
        return 'Not all rows have the same number of columns!'
def validate_columns(input_file):

    frequencies = defaultdict(int)
    duplicates = ''    
    if isinstance(input_file,str):
      
    # open with universal newline mode enabled to prevent csv.Error: new-line character seen in unquoted field
        with open(input_file, 'rU') as csvfile:
            file_reader = csv.reader(csvfile)
            # check for duplicate column names
            first_line = file_reader.next()
            for column in first_line:
                frequencies[column] += 1
                if frequencies[column] == 2:
                    duplicates = duplicates + column + ','

            column_count = len(frequencies)
            if column_count <2:
                raise NoDataError("Data file contains fewer than 2 columns!")
            if duplicates != '':
                raise DuplicateColumnError('duplicate column names:' + duplicates[0:-1])
            # check for proper number of columns in every row
            row_count = 0
            for row in file_reader:
                row_count += 1
                if len(row) != column_count:
                    raise ColumnMismatchError
            if row_count < 1:
                raise NoDataError("Data file contains fewer than 2 rows!")




if __name__ == '__main__':
    #    validate_columns("samples/names.csv")
    validate_columns("samples/SalesJan2009.csv")
    validate_columns("samples/tooFew.csv")
    
    validate_columns("samples/Sacramentorealestatetransactions_a.csv")
