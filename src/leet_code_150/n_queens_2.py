class Solution:
    def totalNQueens(self, n: int) -> int:
        return count_positions(n, 0, [])


def count_positions(n, i, queens):
    if i == n:
        return 1

    return sum([
        count_positions(n, i + 1, queens + [(i, j)])
        for j in range(n)
        if safe_position(i, j, queens)
    ])

def safe_position(i, j, existing_queens):
    for queen_i, queen_j in existing_queens:
        if (i == queen_i or
                j == queen_j or
                j == queen_j + (i - queen_i) or
                j == queen_j - (i - queen_i)):
            return False
    else:
        return True
