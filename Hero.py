from maps import tiles
from random import randint
from tkinter import *
from default import HeroHealthDefault, FILEPATH


class Hero(HeroHealthDefault):
    def __init__(self, level=1):
        super().__init__()
        self.level = level
        self.hero_position = [0, 0]
        self.moveTime = 1
        self.heroStrike = ''
        self.heroChar = {
            "character": "Hero",
            "position": self.hero_position,
            'hp': self.HERO_HP,
            'dp': self.HERO_DP,
            'sp': self.HERO_SP,
        }

    def createHero(self, canva, IMG_SIZE):
        x = self.hero_position[0] * IMG_SIZE
        y = self.hero_position[1] * IMG_SIZE

        if self.heroChar['hp'] > 0:
            canva.create_image(
                x, y, image=self.heroface, anchor=NW)
        else:
            self.hero_position = [-1, -1]

    def moveHero(self, img, x=0, y=0):
        layoutArray = tiles
        self.img = img
        self.heroface = PhotoImage(
            file=f"{FILEPATH}{img}.png")

        xs = self.hero_position[0]
        ys = self.hero_position[1]

        if x and layoutArray[ys][xs + x] == 'o':
            self.hero_position = [xs + x, ys]

        if y and layoutArray[ys + y][xs] == 'o':
            self.hero_position = [xs, ys + y]
        self.moveTime += 1
        if self.moveTime == 3:
            self.moveTime = 1

    def strikeEnemy(self, skeleton):
        for i, character in enumerate(skeleton.allCharacters):
            if character["position"] == self.hero_position:
                if character['hp'] > 0:
                    character['hp'] = character['hp'] - 5
                else:
                    character['hp'] = 0
