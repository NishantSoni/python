import math
import random


class Player:
    """ A class defines the player """

    def __init__(self, letter) -> None:
        self.letter = letter

    def get_move(self):
        pass


class RandomComputerPlayer(Player):
    """ 
    A class which Inherits the Player class and responsible for handling the 
    Random input.
    """

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    """ 
    A class which inherits the Player class
    It is responsible for handling the user input.
    """

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None

        while not valid_square:
            square = input(self.letter + '\'s turn. Input move [0-8]:')

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square, try again!")

        return val
