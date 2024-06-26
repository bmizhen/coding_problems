"""
TicTacToe
simulateGame(n: int)
n x n board
2 AI players - play randomly, any valid square
print winner or tie

winner:
- n in a row
- n in a column
- n in a diagonal
"""

from random import randint
from pprint import pprint


def find_a_move(board) -> tuple[int, int]:
    odds = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            odds += 1
            if board[i][j] < 0:
                # if randint(0, len(board) ** 2 - 1) < odds:
                return i, j


def simulateGame(n: int) -> int:
    """ Returns -1 for a tie, 1 for player 1, 0 for player 0"""

    # -1 is empty, 1 for player 1, 0 for player 0
    board = [[-1] * n for _ in range(n)]

    empty_cells = n ** 2

    player_turn = 0

    while True:
        i, j = find_a_move(board)
        print(player_turn, i, j)
        board[i][j] = player_turn
        empty_cells -= 1
        winner = have_winner(board, player_turn)
        player_turn = 1 if player_turn == 0 else 0
        if winner > -1:
            pprint(board)
            return winner
        if empty_cells == 0:
            pprint(board)
            return -1


# TODO: O(n) pass the last move, only check those rows
# TODO: for O(1) time keep row objects
def have_winner(board, player_turn) -> int:
    for row in board:
        if all(player_turn == e for e in row):
            print('row')
            return player_turn

    for col in range(len(board)):
        if all(board[i][col] == player_turn for i in range(len(board))):
            print('col')
            return player_turn

    if all(board[i][i] == player_turn for i in range(len(board))):
        print('d1')
        return player_turn

    if all(board[i][len(board) - i - 1] == player_turn
           for i in range(len(board))):
        print('d2')
        return player_turn

    return -1


"""
if 3 empty squares:
    1: 1/3
    2: 2/3 * 2/3 = 4/9
    3: 1 - 1/3 - 4/9 = 2/9
"""

# print(simulateGame(1))
# print(simulateGame(2))
print(simulateGame(3))
