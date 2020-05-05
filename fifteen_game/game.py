# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle
import random


# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of: 
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    field = [number for number in range(0, 16)]
    field.append(EMPTY_MARK)
    random.shuffle(field)
    return field


def print_field(field):
    for i in range(0, 16, 4):
        print(field[i:i+4])


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    pass


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    pass


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move.
    """
    pass


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    print_field(shuffle_field())


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    main()