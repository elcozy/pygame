# from Layout import *
from random_character import Random
from tkinter import *
import random
import numpy as np
from hero import Hero
from characters import CharacterMain


class GameLayout():

    def __init__(self, skeletons, hero, IMG_SIZE, stats):
        self.hero = hero
        self.skeletons = skeletons
        self.stats = stats
        self.maxHeroHp = hero.MAXHERO_HP
        self.maxSkeletonHp = 0

    def createInfo(self, canva,  left, bottom):
        heroStat = self.hero.heroChar
        level = self.stats.level
        canva.create_text(180, bottom + 20,  fill="darkblue", font="Times 20 italic bold",
                          text=f'{heroStat["character"]} (Level {level}) HP: {heroStat["hp"]}/{self.maxHeroHp} | DP: {heroStat["dp"]} | SP: {heroStat["sp"]}')
        # print('My health is here')

    def createInfoEnemy(self, canva,  left, bottom, char):
        self.maxEnemyHp = self.skeletons.allCharacters[char]['hp']

        enemyStat = self.skeletons.allCharacters[char]
        level = self.stats.level
        canva.create_text(180, bottom + 40,  fill="darkblue", font="Times 20 italic bold",
                          text=f'{enemyStat["character"]} (Level {level}) HP: {enemyStat["hp"]}/{self.maxEnemyHp} | DP: {enemyStat["dp"]} | SP: {enemyStat["sp"]}')
