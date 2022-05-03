from random import randint
from tkinter import *
from random import randint
from maps import tiles
import default

FILEPATH = default.FILEPATH


class BossHealthDefault():
    def __init__(self, level, characters='None'):
        self.characters = characters
        self.level = level
        self.boss_hp = (2 * self.level) * (randint(1, 6) + randint(1, 6))
        self.boss_dp = (self.level / 2) * \
            (randint(1, 6) + (randint(1, 6) / 2))
        self.boss_sp = self.level * randint(1, 6) + self.level
        self.boss_img = PhotoImage(file=f"{FILEPATH}boss.png")


class Boss(BossHealthDefault):
    """Class for the Boss character"""

    def __init__(self, level, characters):
        super().__init__(level, characters)
        self.boss_created = False

    def create_enemies(self):
        """"Creating enemies"""

        # Generating random number from 0 - 10
        random_number = randint(0, 9)

        while self.boss_created is False:
            # Assigning to variables here
            random_arr_boss = [random_number, randint(0, 9)]
            boss_object = self.characters.setEnemy(
                'boss', random_arr_boss)

            if tiles[random_arr_boss[1]][random_arr_boss[0]] == 'o':
                if not random_arr_boss[1] == random_arr_boss[0] == 0:
                    # Making sure the enemies don't land in the hero box
                    if not (random_arr_boss[0] < 3 and random_arr_boss[1] < 3):
                        self.characters.setCharacter(boss_object)
                        self.boss_created = True
