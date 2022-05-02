# from Layout import *
from random_character import Random
from tkinter import *
import random
import numpy as np
from hero import Hero
from characters import Skeletons


class GameLayout():

    def __init__(self, skeletons, hero, IMG_SIZE):
        self.hero = hero
        self.skeletons = skeletons
        self.currentLevel = 1

    def createInfo(self, canva,  left, bottom):
        heroStat = self.hero.heroChar
        self.currentLevel = self.hero.level
        # print(heroStat)
        canva.create_text(180, bottom + 20,  fill="darkblue", font="Times 20 italic bold",
                          text=f'{heroStat["character"]} (Level {self.currentLevel}) HP: {heroStat["hp"]}/10 | DP: {heroStat["dp"]} | SP: {heroStat["sp"]}')
        # print('My health is here')

    def createInfoEnemy(self, canva,  left, bottom, char):
        enemyStat = self.skeletons.allCharacters[char]
        canva.create_text(180, bottom + 40,  fill="darkblue", font="Times 20 italic bold",
                          text=f'{enemyStat["character"]} (Level {self.currentLevel}) HP: {enemyStat["hp"]}/10 | DP: {enemyStat["dp"]} | SP: {enemyStat["sp"]}')
