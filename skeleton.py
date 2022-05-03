from time import time, sleep
from random import randint, sample, random
import numpy as np
from tkinter import *
from maps import tiles
from default import SkeletonHealthDefault, FILEPATH
# import main

layoutArray = tiles

# FILEPATH = 'assets/img/'

# characters = main.characters


class SkelHealthDefault():
    def __init__(self, level):
        self.level = level
        self.skeleton_hp = (2 * self.level) * randint(1, 6)
        self.skeleton_dp = (self.level / 2) * randint(1, 6)
        self.skeleton_sp = self.level * randint(1, 6)
        self.skeleton_image = PhotoImage(
            file=f"{FILEPATH}skeleton.png")


class Skeleton(SkeletonHealthDefault):

    def __init__(self, level, characters='None'):
        super().__init__(level)
        self.characters = characters
        self.skelCreated = False
        self.enemy = 0
        self.enemiesNeeded = self.characters.enemiesNeeded

    def create_enemies(self):
        # Generating random number from 0 - 10
        print(self.level, self.skeleton_hp, 'dshp')

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
