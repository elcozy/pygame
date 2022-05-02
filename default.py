import random
from random import randint
from tkinter import *

FILEPATH = 'assets/img/'


class HeroHealthDefault():
    def __init__(self):
        self.img = "hero-down"
        self._HERO_HPCALC = 20 + 3 * randint(1, 6)
        self.HERO_HP = self._HERO_HPCALC
        self.MAXHERO_HP = self._HERO_HPCALC
        self.HERO_DP = 2 * randint(1, 6)
        self.HERO_SP = 5 + randint(1, 6)
        self.heroface = PhotoImage(
            file=f"{FILEPATH}{self.img}.png")


class SkeletonHealthDefault():
    def __init__(self, level=1):
        self.level = level
        self.SKELETON_HP = (2 * self.level) * randint(1, 6)
        self.SKELETON_DP = (self.level / 2) * randint(1, 6)
        self.SKELETON_SP = self.level * randint(1, 6)
        self.skeletonImage = PhotoImage(
            file=f"{FILEPATH}skeleton.png")

    def __getitem__(self):
        return {
            # "character": f"{character}{enemyCount}",
            'direction': 'forward',
            'key': FALSE,
            # "position": position,
            'hp': self.SKELETON_HP,
            'dp': self.SKELETON_DP,
            'sp': self.SKELETON_SP
        }


class BossHealthDefault():
    def __init__(self, level=1):
        self.level = level
        self.BOSS_HP = (2 * self.level) * (randint(1, 6) + randint(1, 6))
        self.BOSS_DP = (self.level / 2) * (randint(1, 6) + (randint(1, 6) / 2))
        self.BOSS_SP = self.level * randint(1, 6) + self.level
        self.boss_img = PhotoImage(file=f"{FILEPATH}boss.png")

    def __getitem__(self):
        return {"character": f"Boss",
                'direction': 'forward',
                # "position": position,
                'key': FALSE,
                'hp': self.BOSS_HP,
                'dp': self.BOSS_DP,
                'sp': self.BOSS_SP
                }
