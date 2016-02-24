# -*- coding: utf-8 -*-

from random import shuffle # see https://docs.python.org/2/library/random.html
from sys import version_info

if version_info[0] == 2:
    input_function = raw_input
else:
    input_function = input

EMPTY_MARK = 'empty'

def shuffle_field():
    f = [x for x in range(1,16)]
    f.append(EMPTY_MARK)
    winner_field = f[:]
    shuffle(f)
    return f,winner_field


def print_field(field):
    for i in range(0,16,4):
        row = ''
        for j in range(i,i+4):
            row += str(field[j]) + '\t'
        print (row)





def is_game_finished(field,winner_field):
    if field == winner_field:
        return True
    else:
        return False


def perform_move(field, key):
    i = field.index(EMPTY_MARK)
    if key.lower() == 'w':
    	if i not in range(0,4):
    		field[i],field[i-4] = field[i-4],field[i]
    	else:
    	    raise IndexError

    elif key.lower() == 's':
    	if i not in range(12,16):
    		field[i],field[i+4] = field[i+4],field[i]
    	else:
    	    raise IndexError

    elif key.lower() == 'a':
    	if i not in range(0,13,4):
    		field[i],field[i-1] = field[i-1],field[i]
    	else:
    	    raise IndexError

    elif key.lower() == 'd':
    	if i not in range(3,16,4):
    		field[i],field[i+1] = field[i+1],field[i]
    	else:
    	    raise IndexError

        #else:
         #   print('\nВы ошиблись при выборе клавиши управления.')

def handle_user_input():
    movement = input_function('\nВведите направление движения в формате WSAD: ')
    return movement


def main():
    print('\nДобро пожаловать в игру Пятнашки\n\n\
Управление движением пустого квадрата осуществляется по схеме:\n\
"w" - вверх, "s" - вниз,\n\
"a" - влево, "d" - вправо\n\n')
    field,winner_field = shuffle_field()
    print_field(field)
    while not is_game_finished(field,winner_field):
        try:
            perform_move(field,handle_user_input())
            print_field(field)

        except Exception as ex:
            print ('\nНельзя двигать квадрат за пределы поля!')

    else:
        print ('\nПоздравляю, Вы выиграли!')

# see http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    main()