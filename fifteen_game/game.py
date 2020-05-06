# -*- coding: utf-8 -*-
import random

EMPTY_MARK = 'x'

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
    correct_field = [i for i in range(0, 17)]
    correct_field[-1] = EMPTY_MARK
    return True if field == correct_field else False


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