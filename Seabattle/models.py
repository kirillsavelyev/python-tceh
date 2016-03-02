
from utils import get_input_function

__author__ = 'savelyevka'


class Storage(object):
    obj = None
    players = None
    field = None
    shots = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.players = []
            cls.shots = []
            cls.field = Field()
        return cls.obj


class Field(object):
    INITIAL_STATE = '.'
    # нужно два поля для хранения выстрелов каждого из игроков
    # или одно большое на двоих???

    def __init__(self, size, ship_q):
        self.size = size
        self.ship_q = ship_q
        self.field = []

        for x in range(self.size):
            row = []
            for i in range(self.size):
                row.append(self.__class__.INITIAL_STATE)
            self.field.append(row)

    def __repr__(self):
        pass
        # return self.size, self.ship_q

    def print_field(self):
        for i in range(self.size):
            row = ''
            for j in range(self.size):
                row += str(self.field[j]) + ' '
            print(row)

    # метод end_of game проверяет значения О в массиве поля


class Player(object):
    def __init__(self, objects, name, turn):
        self.name = name
        self.turn = objects.players.index(self.name)
        # очередь приравнивает к индексу записи в массиве players

    def __str__(self):
        return self.name

    # метод генерирует поле для игрока (у каждого свое поле)


class Ship(object):
    HOR = '-'
    VER = '|'

    def __init__(self, size, coordinate, orientation):
        self.size = size
        self.coordinate = coordinate
        self.orientation = orientation

    # метод генерирует координаты корабля на поле по введенным значениям (ориентация и пр.)

    def damage(self):
        pass


class Shot(object):
    def __init__(self, player, coordinate):
        self.player = player
        self.coordinate = coordinate
        # self.hit = hit

    @classmethod
    def shot(cls):
        pass
        # метод прописывает коорднинаты выстрела в массив
        # сравнивая с координатами корабля
        # если совпадает, то отметка Х, иначе О



