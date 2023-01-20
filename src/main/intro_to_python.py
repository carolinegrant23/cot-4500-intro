from tarfile import DIRTYPE
import numpy as np


matrix = np.identity(3, dtype=int)


for row in matrix:
    row_as_text = ''
    for cell in row:
        row_as_text = row_as_text + str(cell) + ' ' 
    print(row_as_text)





for i, row in enumerate(matrix):
    row_as_text = ''
    for j, cell in enumerate(row):
        if i != j: 
            cell = 3 + cell 
        row_as_text = row_as_text + str(cell) + ' '
    print(row_as_text)


new_matrix = np.delete(matrix, 2, 1) 

for i, row in enumerate(new_matrix):
    row_as_text = ''
    for j, cell in enumerate(row):
        if i != j: 
            cell = 3 + cell 
        row_as_text = row_as_text + str(cell) + ' '
    print(row_as_text)





