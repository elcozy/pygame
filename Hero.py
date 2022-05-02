from maps import tiles
from random import randint
from tkinter import *
from skeleton import Skeletons


class Hero():
    def __init__(self, filePath):
        self.FILEPATH = filePath
        self.hero_position = [0, 0]
        self.level = 1
        self.img = "hero-down"
        self.heroface = PhotoImage(
            file=f"{self.FILEPATH}{self.img}.png")
        self.HP = 20 + 3 * randint(1, 6)
        self.DP = 2 * randint(1, 6)
        self.SP = 5 + randint(1, 6)
        self.moveTime = 1

    def herosHealth(self):
        return {
            "character": "Hero",
            "position": self.hero_position,
            'hp': self.HP,
            'dp': self.DP,
            'sp': self.SP,
            'level': self.level
        }

    def createHero(self, canva, IMG_SIZE):
        x = self.hero_position[0] * IMG_SIZE
        y = self.hero_position[1] * IMG_SIZE
        if self.HP > 0:
            canva.create_image(
                x, y, image=self.heroface, anchor=NW)

    def moveHero(self, img, x=0, y=0):
        layoutArray = tiles
        self.img = img
        self.heroface = PhotoImage(
            file=f"{self.FILEPATH}{img}.png")

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
        print("Striking enemy")
        if self.hero_position in skeleton.skeletons:
            stikeEnemyIndex = skeleton.skeletons.index(self.hero_position)
            print(
                f'Strikkkk {skeleton.allCharacters[stikeEnemyIndex]["character"]}')
            skeleton.allCharacters[stikeEnemyIndex]['hp'] = skeleton.allCharacters[stikeEnemyIndex]['hp'] - 5
            print(skeleton.allCharacters)

        else:
            strikeEnemyIndex = 'None'
