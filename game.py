from board import Board
from car import Car
from helper import load_json
import sys


class Game:
    """
    The class receives a game board (object of type Board) and runs a
    game of rush hour.
    """
    COLORS = ['Y', 'B', 'O', 'G', 'W', 'R']
    MOVES = ['u', 'd', 'l', 'r']
    INPUT_MSG = "Please choose car to move, and direction. Enter '!' to exit."
    ERROR_MSG = 'the input is invalid, try again.'
    WIN_MSG = 'Good job! You won the game!'
    END_STR = 'out'
    END_MSG = 'bye!'

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.game_board = board

    def __single_turn(self):
        """
        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.
        """
        while True:
            user_input = input(Game.INPUT_MSG)
            if user_input == "!":
                return Game.END_STR
            elif len(user_input) != 3 or user_input[0] not in Game.COLORS or \
                    user_input[1] != ',' or user_input[2] not in Game.MOVES:
                print(Game.ERROR_MSG)
                continue
            else:
                if not self.game_board.move_car(user_input[0], user_input[2]):
                    print(Game.ERROR_MSG)
                    continue
                else:
                    break

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        final_cord = self.game_board.target_location()
        while not self.game_board.cell_content(final_cord):
            print(self.game_board)
            if self.__single_turn() == Game.END_STR:
                print(Game.END_MSG)
                return
        print(self.game_board)
        print(Game.WIN_MSG)


COLORS = ['Y', 'B', 'O', 'G', 'W', 'R']


def create_and_add_cars(board, info):
    """
    This function load cars information from Json file and adds the valid
    cars to the board of the game.
    :param info: a dictionary with the colors of the cars as keys , and
    list of 3 attributes (length, start coordinate and orientation) as values.
    :param board: and object type of Board class
    :return: None
    """
    for name, attributes in info.items():
        location_cord = (attributes[1][0], attributes[1][1])
        if name in COLORS and attributes[0] in range(2, 5) \
                and attributes[2] in range(2):
            car = Car(name, attributes[0], location_cord, attributes[2])
            board.add_car(car)


if __name__ == "__main__":
    file_path = sys.argv[1]
    info_dict = load_json(file_path)
    game_board = Board()
    rush_hour = Game(game_board)
    create_and_add_cars(game_board, info_dict)
    rush_hour.play()
    sys.exit(0)

