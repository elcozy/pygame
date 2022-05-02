from random import randint
from tkinter import *
from random_character import Random
from maps import tiles
import default

FILEPATH = default.FILEPATH


class BossHealthDefault():
    def __init__(self, characters='None'):
        self.characters = characters
        self.level = 1
        self.BOSS_HP = (2 * self.level) * (randint(1, 6) + randint(1, 6))
        self.BOSS_DP = (self.level / 2) * (randint(1, 6) + (randint(1, 6) / 2))
        self.BOSS_SP = self.level * randint(1, 6) + self.level
        self.boss_img = PhotoImage(file=f"{FILEPATH}boss.png")


class Boss(BossHealthDefault):

    def __init__(self, characters):
        super().__init__(characters)
        self.bossCreated = False

    def createEnemies(self, canva):

        # Generating Random number from 0 - 10
        xRand = Random.randomInt()

        while self.bossCreated == False:
            # Assigning to variables here
            randomArrBoss = [xRand, randint(0, 9)]
            bossObject = self.characters.setEnemy(
                'boss', randomArrBoss)

            if tiles[randomArrBoss[1]][randomArrBoss[0]] == 'o':
                if not (randomArrBoss[1] == randomArrBoss[0] == 0):
                    # Making sure the enemies don't land in the hero box
                    if not (randomArrBoss[0] < 3 and randomArrBoss[1] < 3):
                        self.characters.setCharacter(bossObject)
                        self.bossCreated = True
