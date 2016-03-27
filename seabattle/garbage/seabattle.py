
from models import Storage
from commands import *

from base import get_input


def globalcheck(id):
    x = 0
    c = 0
    for obj in Storage.shots:
        if obj.player_n == id and obj.status is True:
            x += 1
    return x == len(Storage.ships[id])


def move(player_id):
    inp = get_input_function()
    print ('\n\n\n')
    print("It is turn of player {}".format(Storage.players[player_id]))
    shot = ShotCommand(player_id)
    print("ITS YOUR SHIPS")
    ShipCommand.show_ships(player_id)
    print("ITS YOUR MOVES")
    shot.show_moves(player_id)
    if shot.make_move(
            inp('Your move: '),
            PlayerCommand.enemy(player_id)
    ) is True:
        print('Player {} is LUCKY!'.format(Storage.players[player_id]))
        if globalcheck(player_id) is True:
            print('GAME IS ENDED')
            print('Player {} WINS!'.format(Storage.players[player_id]))
            raise GeneratorExit
        else:
            move(player_id)


def main():
    storage = Storage()
    FieldCommand()
    PlayerCommand()

    while True:
        try:
            for player_id, val in enumerate(storage.players):
                move(player_id)

        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()
