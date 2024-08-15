from pprint import pprint
from typing import Any


def rotate_zip(matrix: list[list[Any]]) -> list[list[Any]]:
    matrix.reverse()

    return list(map(list, zip(*matrix)))


def rotate_transpose(matrix: list[list[Any]]) -> list[list[Any]]:
    matrix.reverse()

    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


rotate = rotate_zip

pprint(rotate([]))
pprint(rotate([[1]]))
pprint(rotate([[1, 2], [3, 4]]))
pprint(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# 1 2  3 4  3 1
# 3 4  1 2  4 2

# 1 2 3      7 8 9      7 4 1
# 4 5 6      4 5 6      8 5 2
# 7 8 9      1 2 3      9 6 3
