# mat1 (2x3 matrix):
#
# [1, 0, 0]
# [0, 0, 3]
# mat2 (3x2 matrix):
#
# [1, 2]
# [0, 0]
# [0, 4]
from pprint import pprint

M1 = [
    [1, 0, 0],
    [0, 0, 3]
]

M2 = [
    [1, 2],
    [0, 0],
    [0, 4]
]

def sparse_mult(m1, m2):
    result = [[0] * len(m2[0]) for _ in m1]

    rows = [
        [(i, x) for i, x in enumerate(m1_row)]
        for m1_row in m1
    ]

    cols = [
        [(i, y) for i, y in enumerate(m2_col)]
        for m2_col in zip(*m2)
    ]

    def row_by_col(row, col):
        sum = 0
        col_ptr = 0
        row_ptr = 0

        while col_ptr < len(col) and row_ptr < len(row):
            y_i, y = col[col_ptr]
            x_i, x = row[row_ptr]
            if y_i == x_i:
                sum += x * y
                col_ptr += 1
                row_ptr += 1
            elif y_i < x_i:
                col_ptr += 1
            else:
                row_ptr += 1
        return sum

    for row in range(len(result)):
        for col in range(len(result[0])):
            result[row][col] = row_by_col(rows[row], cols[col])

    return result

pprint(sparse_mult(M1, M2))

