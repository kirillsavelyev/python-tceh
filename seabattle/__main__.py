# -*- coding: utf-8 -*-

from __future__ import print_function
from collections import OrderedDict

from classes import *


class GameController(object):
    SHIP_RULES = OrderedDict([(4, 1)])
    # , (3, 2), (2, 3), (1, 4)

    def __init__(self):
        self.players = []
        player1 = Player()
        self.players.append(player1)
        player2 = Player()
        self.players.append(player2)

        self.field = Field(10)

        for player in self.players:
            player.create_ships(self.SHIP_RULES, self.field)

    def check_game_status(self):
        for player in self.players:
            if all(not ship.afloat for ship in player.ships):
                return False
        return True

    def start_game(self):
        next_shooter = False

        shooter, enemy = self.players

        # начало стрельбы
        print('\n\n', '{}, your first!'.format(shooter.name))
        try:
            while self.check_game_status():
                if next_shooter:
                    shooter, enemy = enemy, shooter
                    print('\n\n', '{}, your turn!'.format(shooter.name))
                    self.field.display_shooter_field(shooter)

                self.field.display_enemy_field(shooter)
                shot = shooter.shooting(self.field, enemy.ships)
                if shot.hit:
                    ship = enemy.take_a_hit(shot.coordinate)
                    print('\n', 'You hit!')
                    if not ship.afloat:
                        print('\n', 'Ship had been destroyed!')
                next_shooter = not shot.hit

            print('Congratulations %s, you won!' % shooter)

        except KeyboardInterrupt:
            print('Error')

        print('End of Game')


if __name__ == '__main__':
    game = GameController()
    game.start_game()
