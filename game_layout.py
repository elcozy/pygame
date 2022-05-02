# from Layout import *
from random_character import Random
from tkinter import *
import random
import numpy as np
from hero import Hero
from skeleton import Skeletons


class GameLayout():

    def __init__(self, hero, heroHealth, IMG_SIZE):
        self.heroHealth = heroHealth
        self.hero = hero
        self.skeletons = []

    def createInfo(self, canva,  left, bottom):
        heroStat = self.heroHealth
        # print(heroStat)
        canva.create_text(180, bottom + 20,  fill="darkblue", font="Times 20 italic bold",
                          text=f'Hero (Level {heroStat["level"]}) HP: {heroStat["hp"]}/10 | DP: {heroStat["dp"]} | SP: {heroStat["sp"]}')
        # print('My health is here')

    def createInfoEnemy(self, canva,  left, bottom, char):
        heroStat = self.heroHealth
        # print(heroStat)
        canva.create_text(180, bottom + 40,  fill="darkblue", font="Times 20 italic bold",
                          text=f'Skeleton (Level {heroStat["level"]}) HP: {heroStat["hp"]}/10 | DP: {heroStat["dp"]} | SP: {heroStat["sp"]}')
        # print('My health is here')
