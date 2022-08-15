import time
from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    """
    This class is responsible for playing the TicTacToe game played by user
    and the computer.
    """

    def __init__(self):
        # represent 3*3 board
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        # Print the board
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Show numbers for selecting the option for a perticular square.
        # 0 | 1 | 2
        # 3 | 4 | 5
        # 6 | 7 | 8
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # returns all the LIST of square which is not selected yet.
        return [i for (i, spot) in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        # returns the empty square in the board.
        return ' ' in self.board

    def num_empty_squares(self):
        # Returns the count of empty squares.
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move, then make move and return true, else false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check if 3 in a row anywhere
        # we have to check of row_wise, column_wise and diagonal wise these.

        # check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all(letter == spot for spot in row):
            return True

        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all(letter == spot for spot in column):
            return True

        # check diagonals
        # only if square value is an even number 0, 2, 4, 6, 8
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all(letter == spot for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(letter == spot for spot in diagonal2):
                return True

        return False


def play(game, x_player, o_player, print_game=True):
    # Method returns the winner of the game or else NONE for tie.
    if print_game:
        game.print_board_nums()

    # starting letter
    letter = 'X'

    # iterate below loop while the game has still empty squares
    # (We dont have to worry about the winner because we will just
    # return that which breaks the loop)
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to {square}")
                game.print_board()
                print('')  # it will print the empty line.

            if game.current_winner:
                if print_game:
                    print(letter + " won the game!")
                return letter

            # after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'

            # some break
            time.sleep(0.8)

    if print_game:
        print('it\'s tie')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    ttt = TicTacToe()
    play(ttt, x_player, o_player, print_game=True)
