
from base import get_input

__author__ = 'savelyevka'


class Player(object):
    def __init__(self, human=True):
        self._human = human
        self._ships = []
        self._shots = []
        self.name = get_input('Please enter Player name: ')

    def __str__(self):
        return self.name

    @property
    def ships(self):
        return self._ships

    @property
    def shots(self):
        return self._shots

    def create_ships(self, rules, field):
        for length, number in rules.items():
            for i in range(number):
                self.new_ship(field, length)

    def new_ship(self, field, length):
        try:
            start = get_input('Input start position for \
{}-ship in format ROW,COL (ex. 1,2): '.format(length))
            d = start.split(',')
            row_start = int(d[0]) - 1
            col_start = int(d[1]) - 1
            ship = []
            pos = [row_start, col_start]
            if (
                        self.is_duplicate(pos) is True or
                        self.check_perimeter(pos, field.size)):
                raise ValueError
            else:
                ship.append(pos)

            if int(length) > 1:
                direction = get_input('Input directions for \
{}-ship (WASD):'.format(length))
                it = int(length) - 1
                while it > 0:
                    if direction == 'w':
                        pos = [row_start - it, col_start]
                    elif direction == 'a':
                        pos = [row_start, col_start - it]
                    elif direction == 's':
                        pos = [row_start + it, col_start]
                    elif direction == 'd':
                        pos = [row_start, col_start + it]

                    if (
                                self.is_duplicate(pos) is True or
                                self.check_perimeter(pos, field.size)):
                        raise ValueError
                    else:
                        ship.append(pos)
                        it -= 1

            self._ships.append(Ship(ship))

        except ValueError:
            print('Wrong position, try again!')
            self.new_ship(field, length)
        except IndexError:
            print('Wrong direction, try again!')
            self.new_ship(field, length)

    def is_duplicate(self, pos):
        error_list = []
        for ship in self.ships:
            for cord in ship.cords:
                error_list.append([cord[0], cord[1]])
                error_list.append([cord[0] - 1, cord[1] - 1])
                error_list.append([cord[0] + 1, cord[1] - 1])
                error_list.append([cord[0] - 1, cord[1] + 1])
                error_list.append([cord[0] + 1, cord[1] + 1])
        if pos in error_list:
            return True
        else:
            return False

    @staticmethod
    def check_perimeter(cord, field_size):
        if (
                    cord[0] < 0 or
                    cord[1] < 0 or
                    cord[0] >= field_size or
                    cord[1] >= field_size):
            return True

    def shooting(self, field, enemy_ships):
        def valid_shoot_position():
            return (shot is not None) and (shot not in self._shots)

        shot = None
        while not valid_shoot_position():
            try:
                cords_input = get_input('Enter coordinates your shot (x, y): ')
                c = cords_input.split(',')
                row = int(c[0]) - 1
                col = int(c[1]) - 1
                cords = [row, col]
                if self.check_perimeter(cords, field.size):
                    raise ValueError()
                # if (row < 0 or col < 0) or \
                #         (row >= field.size or col >= field.size):
                #     raise ValueError()

                shot = Shot(cords, enemy_ships)
                self._shots.append(shot)
                return shot
            except (IndexError, ValueError):
                print('Wrong input, try again!')

    def take_a_hit(self, shot):
        for ship in self._ships:
            if shot in ship.cords:
                try:
                    ship.do_damage(shot)
                    return ship
                except ValueError:
                    pass


class Field(object):
    INITIAL_STATE = '~'
    SHIP_STATE = '='
    MISS = 'o'
    HIT = 'x'

    def __init__(self, size):
        self.size = size

    def display_shooter_field(self, shooter):
        print('\n', 'Your ships status...')
        field = []

        for i in range(int(self.size)):
            row = []
            for j in range(int(self.size)):
                row.append(self.__class__.INITIAL_STATE)
            field.append(row)

        for ship in shooter.ships:
            for cord in ship.cords:
                if cord in ship.damage:
                    field[cord[0]][cord[1]] = self.__class__.HIT
                else:
                    field[cord[0]][cord[1]] = self.__class__.SHIP_STATE

        top = ''
        for t in range(int(self.size)):
            top += '\t' + str(t+1)
        print(top)

        for i in range(int(self.size)):
            line = str(i + 1)
            for j in range(int(self.size)):
                line += '\t' + field[i][j]
            print(line)

    def display_enemy_field(self, shooter):
        print('\n', 'Your shoots status...')
        field = []

        for i in range(int(self.size)):
            row = []
            for j in range(int(self.size)):
                row.append(self.__class__.INITIAL_STATE)
            field.append(row)

        for shot in shooter.shots:
            field[shot.coordinate[0]][shot.coordinate[1]] = self.__class__.HIT if shot.hit \
                    else self.__class__.MISS

        top = ''
        for t in range(int(self.size)):
            top += '\t' + str(t+1)
        print(top)

        for i in range(int(self.size)):
            line = str(i + 1)
            for j in range(int(self.size)):
                line += '\t' + field[i][j]
            print(line)


class Ship(object):
    def __init__(self, cords):
        self.cords = cords
        self._damage = []

    @property
    def afloat(self):
        return len(self._damage) < len(self.cords)

    @property
    def damage(self):
        return self._damage

    def do_damage(self, shot):
        if shot in self._damage:
            raise ValueError('Already damaged!')
        self._damage.append(shot)


class Shot(object):
    def __init__(self, coordinate, enemy_ships):
        self.coordinate = coordinate
        self.hit = False

        for ship in enemy_ships:
            if coordinate in ship.cords:
                self.hit = True
