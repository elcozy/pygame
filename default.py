from random import randint
from tkinter import PhotoImage

FILEPATH = 'assets/img/'


class HeroHealthDefault():
    """Default stats for the Hero"""

    def __init__(self):
        self.img = "hero-down"
        self._hero_hp_calc = 20 + 3 * randint(1, 6)
        self.hero_hp = self._hero_hp_calc
        self.max_hero_hp = self._hero_hp_calc
        self.hero_dp = 2 * randint(1, 6)
        self.hero_sp = 5 + randint(1, 6)
        self.heroface = PhotoImage(
            file=f"{FILEPATH}{self.img}.png")


class SkeletonHealthDefault():
    """Default stats for the Skeleton"""

    def __init__(self, level=1):
        self.level = level
        self.skeleton_hp = (2 * self.level) * randint(1, 6)
        self.skeleton_dp = (self.level / 2) * randint(1, 6)
        self.skeleton_sp = self.level * randint(1, 6)
        self.skeleton_image = PhotoImage(
            file=f"{FILEPATH}skeleton.png")

    def __getitem__(self):
        return {
            'direction': 'forward',
            'key': False,
            'hp': self.skeleton_hp,
            'dp': self.skeleton_dp,
            'sp': self.skeleton_sp
        }


class BossHealthDefault():
    """Default stats for the Boss"""

    def __init__(self, level=1):
        self.level = level
        self.boss_hp = (2 * self.level) * (randint(1, 6) + randint(1, 6))
        self.boss_dp = (self.level / 2) * (randint(1, 6) + (randint(1, 6) / 2))
        self.boss_sp = self.level * randint(1, 6) + self.level
        self.boss_img = PhotoImage(file=f"{FILEPATH}boss.png")

    def get_dict_boss(self):
        """Get the dict for boss"""

        return {"character": "Boss",
                'direction': 'forward',
                'key': False,
                'hp': self.boss_hp,
                'dp': self.boss_dp,
                'sp': self.boss_sp
                }
