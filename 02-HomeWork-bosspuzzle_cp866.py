# -*- coding: cp866 -*-

from random import shuffle # see https://docs.python.org/2/library/random.html
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
    f = [x for x in range(1,16)]
    f.append(EMPTY_MARK)
    winner_field = f[:]
    shuffle(f)
    return f,winner_field


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    for i in range(0,16,4):
        row = ''
        for j in range(i,i+4):
            row += str(field[j]) + '\t'
        print (row)





def is_game_finished(field,winner_field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    if field == winner_field:
        return True
    else:
        return False


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    #if key.lower() in ['w','s','a','d']:
    try:
        i = field.index(EMPTY_MARK)
        if key.lower() == 'w':
            if i not in range(0,4):
                field[i],field[i-4] = field[i-4],field[i]

        if key.lower() == 's':
            if i not in range(12,16):
                field[i],field[i+4] = field[i+4],field[i]

        if key.lower() == 'a':
            if i not in range(0,13,4):
                field[i],field[i-1] = field[i-1],field[i]

        if key.lower() == 'd':
            if i not in range(3,16,4):
                field[i],field[i+1] = field[i+1],field[i]

        else:
            print('Вы ошиблись при выборе клавиши управления.')

    except IndexError:
        print ('Неверное направление движения!')
        handle_user_input()


def handle_user_input():
    """
    Handles user input. List of accepted moves:
    'w' - up, 's' - down,
    'a' - left, 'd' - right
    :return: <str> current move.
    """
    movement = input_function('Введите направление движения в формате WSAD: ')
    return movement


def main():
    """
    The main method.
    :return: None
    """
    field,winner_field = shuffle_field()
    print_field(field)
    while not is_game_finished(field,winner_field):
        perform_move(field,handle_user_input())
        print_field(field)
    else:
        print ('Поздравляю, Вы выиграли!')

# see http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    main()