# -*- coding: utf-8 -*-
# see https://docs.python.org/2/library/random.html
from random import shuffle
from sys import version_info

if version_info[0] == 2:
    input_function = raw_input
else:
    input_function = input

EMPTY_MARK = 'empty'


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    f = [x for x in range(1, 16)]
    f.append(EMPTY_MARK)
    shuffle(f)
    return f


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    for i in range(0, 16, 4):
        row = ''
        for j in range(i, i+4):
            row += str(field[j]) + '\t'
        print (row)


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    winner_field = [x for x in range(1, 16)]
    winner_field.append(EMPTY_MARK)
    return field == winner_field


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    i = field.index(EMPTY_MARK)
    if key.lower() == 'w':
        if i not in range(0, 4):
            field[i], field[i-4] = field[i-4], field[i]
        else:
            raise IndexError

    elif key.lower() == 's':
        if i not in range(12, 16):
            field[i], field[i+4] = field[i+4], field[i]
        else:
            raise IndexError

    elif key.lower() == 'a':
        if i not in range(0, 13, 4):
            field[i], field[i-1] = field[i-1], field[i]
        else:
            raise IndexError

    elif key.lower() == 'd':
        if i not in range(3, 16, 4):
            field[i], field[i+1] = field[i+1], field[i]
        else:
            raise IndexError

    else:
        print ('\nУправление только клавишами WSAD.\n')

    return field


def handle_user_input():
    """
    Handles user input. List of accepted moves:
    'w' - up, 's' - down,
    'a' - left, 'd' - right
    :return: <str> current move.
    """
    movement = input_function('\nВведите направление движения в формате WSAD: ')
    return movement


def main():
    """
    The main method.
    :return: None
    """
    print('\nДобро пожаловать в игру Пятнашки\n\n\
Управление движением пустого квадрата осуществляется по схеме:\n\
"w" - вверх, "s" - вниз,\n\
"a" - влево, "d" - вправо\n\n')
    field = shuffle_field()
    print_field(field)
    while not is_game_finished(field):
        try:
            print_field(perform_move(field, handle_user_input()))

        except IndexError:
            print ('\nНельзя двигать квадрат за пределы поля!')

    else:
        print ('\nПоздравляю, Вы выиграли!')

# see http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    main()
