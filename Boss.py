from random import randint
from tkinter import PhotoImage
from default import FILEPATH


class BossHealthDefault():
    """Default heath for the Boss"""

    def __init__(self, level, characters=None):
        self.level = level
        self.characters = characters
        self.boss_hp = (2 * self.level) * (randint(1, 6) + randint(1, 6))
        self.boss_dp = (self.level / 2) * \
            (randint(1, 6) + (randint(1, 6) / 2))
        self.boss_sp = self.level * randint(1, 6) + self.level
        self.boss_img = PhotoImage(file=f"{FILEPATH}boss.png")


class Boss(BossHealthDefault):
    """Class for the Boss character"""

    def __init__(self, level, characters, tiles=None):
        super().__init__(level, characters)
        self.boss_created = False
        self.tiles = tiles

    def create_enemies(self):
        """"Creating enemies"""

        # Generating random number from 0 - 10
        random_number = randint(0, 9)

        while self.boss_created == False:
            # Assigning to variables here
            random_arr_boss = [random_number, randint(0, 9)]
            boss_object = {
                "character": "Boss",
                'direction': 'forward',
                "position": random_arr_boss,
                'key': False,
                'hp': self.boss_hp,
                'dp': self.boss_dp,
                'sp': self.boss_sp
            }
            if self.tiles[random_arr_boss[1]][random_arr_boss[0]] == 'o':
                if not random_arr_boss[1] == random_arr_boss[0] == 0:
                    # Making sure the enemies don't land in the hero box
                    if not (random_arr_boss[0] < 3 and random_arr_boss[1] < 3):
                        self.characters.set_character(boss_object)
                        self.boss_created = True
