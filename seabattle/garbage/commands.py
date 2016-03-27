
from models import *


class BaseCommand(object):
    def __init__(self, **kwargs):
        for key in kwargs:
            st = getattr(Storage, key)
            st.append(kwargs[key])
            setattr(Storage, key, st)


class FieldCommand(BaseCommand):
    def __init__(self):
        input_function = get_input_function()
        size = input_function('Field size: ')
        ship_q = input_function('Ship quality')
        Storage.field = Field(size, ship_q)


class PlayerCommand(BaseCommand):
    def __init__(self):
        input_function = get_input_function()
        for p in range(2):
            player = Player(input_function('\
            Please enter name Player {}: '.format(p+1)))
            Storage.players.append(player)
            Storage.ships.append([])
            print('Start generating ships...')
            ShipCommand.ships_generator(p)

    @staticmethod
    def enemy(player_id):
        for enemy_id in enumerate(Storage.players):
            if enemy_id != player_id:
                return enemy_id


class ShipCommand(BaseCommand):
    def __init__(self):
        pass

    @classmethod
    def new_ship(cls, player_id, length):
        inp = get_input()
        length
        try:
            start = inp('Input start position for \
{}-ship in format ROW,COL (ex. 1,2): '.format(length+1))
            if int(length+1) > 1:
                direction = inp('Input directions for \
{}-ship (WASD):'.format(length+1))
            else:
                direction = 'w'

            d = start.split(',')
            row_start = int(d[0]) - 1
            col_start = int(d[1]) - 1
            ship = []
            it = int(length+1) - 1
            while it >= 0:
                pos = []
                if direction == 'w':
                    pos = [row_start - it, col_start]
                elif direction == 'a':
                    pos = [row_start, col_start - it]
                elif direction == 's':
                    pos = [row_start + it, col_start]
                elif direction == 'd':
                    pos = [row_start, col_start + it]
                if (
                    cls.is_collocate(player_id, pos) is True or
                    pos[0] < 0 or
                    pos[1] < 0 or
                    pos[0] >= int(Storage.field.size) or
                    pos[1] >= int(Storage.field.size)
                ):
                    raise ValueError
                else:
                    ship.append(pos)
                    it -= 1
            Storage.ships[player_id].append(Ship(ship))
        except ValueError:
            print('Wrong position, try again!')
            cls.new_ship(player_id, length)
        except IndexError:
            print('Wrong direction, try again!')
            cls.new_ship(player_id, length)

    @staticmethod
    def find_ship(player_id, fin, **kwargs):
        if 'mode' in kwargs and kwargs['mode'] == 'ships':
            for obj in Storage.ships[player_id]:
                for sh in obj.ship:
                    if sh == fin:
                        return True
        elif 'mode' in kwargs and kwargs['mode'] == 'shouts':
            for obj in Storage.shots:
                if obj.player_n == player_id and obj.cords == fin:
                    return obj
        return False

    @classmethod
    def show_ships(cls, player_id):
        sz = Storage.field.size

        top = '\t'
        for t in range(int(sz)):
            top += str(t+1) + '\t'
        print(top)

        for i in range(int(sz)):
            line = str(i + 1) + '\t'
            for j in range(int(sz)):
                enemy_id = PlayerCommand.enemy(player_id)
                op = cls.check_ship_status(enemy_id, [i, j])
                if cls.find_ship(player_id, [i, j], mode='ships') is not False:
                    if op is True:
                        line += 'X'
                    else:
                        line += '[]'
                else:
                    if op is True:
                        line += 'O'
                    else:
                        line += '~'
                line += '\t'
            print(line)

    @staticmethod
    def is_collocate(player_id, pos):
        errorlist = []
        for obj in Storage.ships[player_id]:
            for sh in obj.ship:
                errorlist.append([sh[0], sh[1]])
                errorlist.append([sh[0] - 1, sh[1] - 1])
                errorlist.append([sh[0] + 1, sh[1] - 1])
                errorlist.append([sh[0] - 1, sh[1] + 1])
                errorlist.append([sh[0] + 1, sh[1] + 1])
        if pos in errorlist:
            return True
        else:
            return False

    @staticmethod
    def check_ship_status(enemy_id, cords):
        if len(Storage.shots) > 0:
            for obj in Storage.shots:
                if enemy_id == obj.player_n and obj.cords == cords:
                    return True
                else:
                    return False
        else:
            return False

    @classmethod
    def ships_generator(cls, player_id):
        for s in range(int(Storage.field.ship_q)):
            cls.show_ships(player_id)
            cls.new_ship(player_id, s)


class ShotCommand(BaseCommand):
    def __init__(self, player_n):
        self.player_n = player_n

    def make_move(self, cords, enemy):
        d = cords.split(',')
        row = int(d[0]) - 1
        col = int(d[1]) - 1
        cords = [row, col]
        status = ShipCommand.find_ship(enemy, cords, mode='ships')

        shot = Shot(self.player_n, cords, status)
        Storage.shots.append(shot)
        # super(ShotCommand, self).__init__(shouts=NSh)
        return status

    @classmethod
    def show_moves(cls, player_id):
        sz = Storage.field.size

        top = '\t'
        for t in range(int(sz)):
            top += str(t+1) + '\t'
        print(top)

        for i in range(int(sz)):
            line = str(i + 1) + '\t'
            for j in range(int(sz)):
                obj = ShipCommand.find_ship(player_id, [i, j], mode='shouts')
                if obj is not False:
                    if obj.status is True:
                        line += 'X'
                    else:
                        line += 'O'
                else:
                    line += '~'
                line += '\t'
            print(line)

