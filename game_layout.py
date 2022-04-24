# from Layout import *
from random_character import Random
from tkinter import *
import random
import numpy as np


class GameLayout():

    def __init__(self, hero, filePath, IMG_SIZE):
        self.filePath = filePath
        self.hero = hero
        self.IMG_SIZE = IMG_SIZE
        self.tiles = []
        self.skeletons = []

        self.diffEnemiesLocation = False
        self.boss = PhotoImage(file=f"{self.filePath}boss.png")
        self.skeleton = PhotoImage(file=f"{self.filePath}skeleton.png")
        self.skeletn1Good = False
        self.skeletn2Good = False
        self.skeletn3Good = False
        self.bossPosition = [0, 0]
        self.bossGood = False

    def createInfo(self, canva,  left, bottom, level, hpLeft, dp,  sp):
        canva.create_text(180, bottom + 20,  fill="darkblue", font="Times 20 italic bold",
                          text=f'Hero (Level {level}) HP: {hpLeft}/10 | DP: {dp} | SP: {sp}')
        # print('My health is here')
