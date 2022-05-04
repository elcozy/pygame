
from random import randint, sample, random
import time
import numpy as np
from tkinter import *
# from maps import MapTiles
from default import SkeletonHealthDefault, BossHealthDefault
import game_constants

# self.tiles = MapTiles().tiles

IMG_SIZE = game_constants.IMG_SIZE

FILEPATH = 'assets/img/'


class CharacterMain():
    last_move_time = time.time()

    def __init__(self, hero=None, level=1, stats='None', tiles=None, skeletonsNeeded=3):

        self.stats = stats
        self.hero = hero
        self.tiles = tiles
        self.skeletons = []
        self.allCharacters = []
        self.enemy = 1
        self.enemiesNeeded = skeletonsNeeded
        self.skeletonStrike = ''
        self.keyRandom = randint(0, self.enemiesNeeded - 1)
        self.skeleton_image = PhotoImage(
            file=f"{FILEPATH}skeleton.png")
        self.boss_img = PhotoImage(file=f"{FILEPATH}boss.png")

    def setCharacter(self, character):
        self.allCharacters.append(character)

    def createEnemies(self, canva):

        for i in range(len(self.allCharacters)):
            x = self.allCharacters[i]['position'][0] * IMG_SIZE
            y = self.allCharacters[i]['position'][1] * IMG_SIZE

            if self.allCharacters[i]['hp'] > 0:
                character = self.allCharacters[i]['character']
                canva.create_image(x, y, image=self.boss_img if character is
                                   'Boss' else self.skeleton_image, anchor=NW)

    def moveSkeletons(self):

        skelt = self.allCharacters

        if len(self.skeletons) != 0:
            for b in range(len(skelt)):
                randomPositions = ['upward', 'downward', 'forward', 'backward']
                randomPositionsB = ['upward', 'downward', 'backward']
                randomPositionsU = ['upward', 'forward', 'backward']
                randomPositionsD = ['downward', 'forward', 'backward']

                if skelt[b]['direction'] is 'forward':
                    if skelt[b]['position'][0] < 9 and self.tiles[skelt[b]['position'][1]][skelt[b]['position'][0] + 1] is 'o':
                        skelt[b]['position'] = [skelt[b]['position']
                                                [0] + 1, skelt[b]['position'][1]]
                        if (skelt[b]['position'][1] < 9 and self.tiles[skelt[b]['position'][1] + 1][skelt[b]['position'][0]] is 'o') or (skelt[b]['position'][1] > 0 and self.tiles[skelt[b]['position'][1] - 1][skelt[b]['position'][0]] is 'o'):
                            skelt[b]['direction'] = randomPositions[randint(
                                0, 2)]
                    else:
                        skelt[b]['direction'] = randomPositions[randint(0, 1)]

                if skelt[b]['direction'] is 'backward':
                    if skelt[b]['position'][0] > 0 and self.tiles[skelt[b]['position'][1]][skelt[b]['position'][0] - 1] is 'o':
                        skelt[b]['position'] = [skelt[b]['position']
                                                [0] - 1, skelt[b]['position'][1]]
                        if (skelt[b]['position'][1] < 9 and self.tiles[skelt[b]['position'][1] + 1][skelt[b]['position'][0]] is 'o') or (skelt[b]['position'][1] > 0 and self.tiles[skelt[b]['position'][1] - 1][skelt[b]['position'][0]] is 'o'):
                            skelt[b]['direction'] = randomPositionsB[randint(
                                0, 2)]
                    else:
                        skelt[b]['direction'] = randomPositions[randint(0, 1)]

                if skelt[b]['direction'] is 'downward':
                    if skelt[b]['position'][1] < 9 and self.tiles[skelt[b]['position'][1] + 1][skelt[b]['position'][0]] is 'o':
                        skelt[b]['position'] = [skelt[b]['position']
                                                [0], skelt[b]['position'][1] + 1]
                        if (skelt[b]['position'][0] < 9 and self.tiles[skelt[b]['position'][1]][skelt[b]['position'][0] + 1] is 'o') or (skelt[b]['position'][0] > 0 and self.tiles[skelt[b]['position'][1]][skelt[b]['position'][0] - 1] is 'o'):
                            skelt[b]['direction'] = randomPositions[randint(
                                1, 3)]
                    else:
                        skelt[b]['direction'] = randomPositions[randint(2, 3)]

                if skelt[b]['direction'] is 'upward':
                    if skelt[b]['position'][1] > 0 and self.tiles[skelt[b]['position'][1] - 1][skelt[b]['position'][0]] is 'o':
                        skelt[b]['position'] = [skelt[b]['position']
                                                [0], skelt[b]['position'][1] - 1]
                        if (skelt[b]['position'][0] < 9 and self.tiles[skelt[b]['position'][1]][skelt[b]['position'][0] + 1] is 'o') or (skelt[b]['position'][0] > 0 and self.tiles[skelt[b]['position'][1]][skelt[b]['position'][0] - 1] is 'o'):
                            skelt[b]['direction'] = randomPositionsU[randint(
                                0, 2)]
                    else:
                        skelt[b]['direction'] = randomPositions[randint(2, 3)]

                print('-------------')

    def updateSkeletons(self):
        self.skeletons = []
        for z in self.allCharacters:
            if z['hp'] > 0:
                self.skeletons.append(
                    z['position'])

            # if len(self.skeletons) is 0:

    def levelUp(self):

        if self.hero.hero_dp < 1:
            self.stats.hero_killed = True
        if len(self.allCharacters) > 0:
            for i, character in enumerate(self.allCharacters):
                if character['key'] is True:
                    key_holder = i
                if character['character'] is "Boss":
                    boss = i

            if self.allCharacters[boss]['hp'] < 1 and self.allCharacters[key_holder]['hp'] < 1:
                print('boss and key holder killed')
                self.stats.levelUp()
                self.stats.level_complete = True

    def strikeHero(self):
        heroArr = self.hero.hero_position

        if heroArr in self.skeletons:
            self.skeletonStrike = self.skeletons.index(heroArr)
        else:
            self.skeletonStrike = ''

        if time.time() - self.last_move_time < 1:
            return
        self.last_move_time = time.time()

        if self.skeletonStrike != '':
            self.skeletonStrike = self.skeletons.index(heroArr)
            self.hero.hero_hp = self.hero.hero_hp - 3

            if self.allCharacters[self.skeletonStrike]["key"]:
                print(
                    f'{self.allCharacters[self.skeletonStrike]["character"]} has the key')
