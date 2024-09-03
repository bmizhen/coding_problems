# tic tac toe game


# class that represents the board
class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    # method that prints the board
    def print_board(self):
        print()
        print(
            f"{'─' * 5}\n".join(
                f"{'┊'.join(row)}\n" for row in self.board),
        )
        print()

    def columns_and_coords(self):
        return [
            (col, [(i, col_index) for i in range(3)])
            for col_index, col in enumerate(zip(*self.board))
        ]

    def rows_and_coords(self):
        return [
            (row, [(row_index, i) for i in range(3)])
            for row_index, row in enumerate(self.board)
        ]

    def diagonals_and_coords(self):
        d1 = [self.board[i][i] for i in range(3)]
        d2 = [self.board[i][2 - i] for i in range(3)]
        d1 = d1, [(i, i) for i in range(3)]
        d2 = d2, [(i, 2 - i) for i in range(3)]
        return [d1, d2]

    def all_lines(self):
        return [*self.rows_and_coords(),
                *self.columns_and_coords(),
                *self.diagonals_and_coords()]

    # method that checks if the board is full
    def is_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def is_empty(self):
        for row in self.board:
            if row.count(' ') != 3:
                return False
        return True

    # method that checks if a player has won
    def check_win(self, player):
        for line, _ in self.all_lines():
            if line.count(player) == 3:
                return True
        return False

    # method that checks if a move is valid
    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    # method that makes a move
    def make_move(self, row, col, player):
        if self.is_valid_move(row, col):
            self.board[row][col] = player
            return True
        return False


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_next_move(self, board: Board):
        row = int(input(f'Player {self.name}, enter row: '))
        col = int(input(f'Player {self.name}, enter column: '))
        return row, col


class AIPlayer(Player):
    def __init__(self, name, symbol):
        super().__init__(name, symbol)

    def get_next_move(self, board: Board) -> tuple[int, int]:
        # if the board is empty take the center
        if board.is_empty():
            # TODO: don't assume 3x3
            return 1, 1

        # if there is a winning move do that
        all_lines = board.all_lines()

        for line, coords in all_lines:
            if line.count(' ') == 1 and line.count(self.symbol) == 2:
                return coords[line.index(' ')]

        # if can block opponent's winning move do that
        for line, coords in all_lines:
            if line.count(' ') == 1 and line.count(self.symbol) == 0:
                return coords[line.index(' ')]

        # otherwise do a random move
        for row in range(3):
            for col in range(3):
                if board.board[row][col] == ' ':
                    return row, col

        raise Exception(' should not be here')


# function that starts the game
def play_game(board):
    # players = [Player('X', 'X'), AIPlayer('O', 'O')]
    players = [AIPlayer('X', 'X'), AIPlayer('O', 'O')]
    player_index = 0
    while True:
        current_player = players[player_index]

        row, col = current_player.get_next_move(board)
        print(f'player {current_player.symbol} goes to {row} {col}')

        print('\n')
        if board.make_move(row, col, current_player.symbol):
            board.print_board()
            if board.check_win(current_player.symbol):
                print(f'Player {current_player.symbol} wins!')
                break
            if board.is_full():
                print("It's a tie!")
                break
            player_index = (player_index + 1) % len(players)
        else:
            print('Invalid move. Try again.')
            raise Exception(f'Move {row, col}')


if __name__ == '__main__':
    # create a board
    board = Board()
    board.print_board()
    # start the game
    play_game(board)
