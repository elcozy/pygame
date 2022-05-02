from time import time, sleep
from random import randint, sample, random
import numpy as np
from tkinter import *
from random_character import Random
from maps import tiles
# import main

layoutArray = tiles

FILEPATH = 'assets/img/'

# characters = main.characters


class SkelHealthDefault():
    def __init__(self, level, characters='None'):
        self.characters = characters
        self.level = level
        self.SKELETON_HP = (2 * self.level) * randint(1, 6)
        self.SKELETON_DP = (self.level / 2) * randint(1, 6)
        self.SKELETON_SP = self.level * randint(1, 6)
        self.skeletonImage = PhotoImage(
            file=f"{FILEPATH}skeleton.png")
        self.enemy = 0


class Skeleton(SkelHealthDefault):

    def __init__(self, level, characters):
        super().__init__(level, characters)
        self.skelCreated = False
        self.enemiesNeeded = self.characters.enemiesNeeded

    def createEnemies(self, canva):
        # Generating Random number from 0 - 10
        print(self.level, self.SKELETON_HP, 'dshp')

        xRand = sample(range(0, 10), 10)
        while self.enemy < self.enemiesNeeded:
            # Assigning to variables here
            randomArr = [xRand[self.enemy], randint(0, 9)]
            skeletonObject = self.characters.setEnemy(
                'skeleton', randomArr, self.enemy)

            # Creating the enemies here
            if layoutArray[randomArr[1]][randomArr[0]] == 'o':
                if not (randomArr[1] == randomArr[0] == 0):
                    # Making sure the enemies don't land in the hero box
                    if not (randomArr[0] < 3 and randomArr[1] < 3):
                        self.characters.setCharacter(skeletonObject)
                        self.enemy += 1
