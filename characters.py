
from random import randint, sample, random
import numpy as np
from tkinter import *
from random_character import Random
from maps import tiles
import time
from default import SkeletonHealthDefault, BossHealthDefault
import constants

layoutArray = tiles

IMG_SIZE = constants.IMG_SIZE

FILEPATH = 'assets/img/'


class CharactersHealthDefault():
    def __init__(self, level=1):
        self.level = 1
        self.SKELETON_HP = (2 * self.level) * randint(1, 6)
        self.SKELETON_DP = (self.level / 2) * randint(1, 6)
        self.SKELETON_SP = self.level * randint(1, 6)
        self.BOSS_HP = (2 * self.level) * (randint(1, 6) + randint(1, 6))
        self.BOSS_DP = (self.level / 2) * (randint(1, 6) + (randint(1, 6) / 2))
        self.BOSS_SP = self.level * randint(1, 6) + self.level
        self.boss_img = PhotoImage(file=f"{FILEPATH}boss.png")
        self.skeletonImage = PhotoImage(
            file=f"{FILEPATH}skeleton.png")


class CharacterMain(CharactersHealthDefault):
    last_move_time = time.time()

    def __init__(self, hero=None, level=1, stats='None', skeletonsNeeded=3):
        super().__init__(level)

        self.stats = stats
        self.hero = hero
        self.skeletons = []
        self.allCharacters = []
        self.enemy = 1
        self.enemiesNeeded = skeletonsNeeded
        self.skeletonStrike = ''
        self.keyRandom = randint(0, self.enemiesNeeded - 1)

    def setEnemy(self, character, position, enemyCount=1):
        key = TRUE if enemyCount == self.keyRandom else FALSE
        if character == 'boss':
            return {
                "character": "Boss",
                'direction': 'forward',
                "position": position,
                'key': FALSE,
                'hp': self.BOSS_HP,
                'dp': self.BOSS_DP,
                'sp': self.BOSS_SP
            }
        if character == 'skeleton':
            return {
                "character": f"{character}{enemyCount}",
                'direction': 'forward',
                'key': key,
                "position": position,
                'hp': self.SKELETON_HP,
                'dp': self.SKELETON_DP,
                'sp': self.SKELETON_SP
            }
        else:
            print("No enemy here")

    def setCharacter(self, character):
        self.allCharacters.append(character)

    def createEnemies(self, canva):

        for i in range(len(self.allCharacters)):
            x = self.allCharacters[i]['position'][0] * IMG_SIZE
            y = self.allCharacters[i]['position'][1] * IMG_SIZE

            if self.allCharacters[i]['hp'] > 0:
                character = self.allCharacters[i]['character']
                canva.create_image(x, y, image=self.boss_img if character ==
                                   'Boss' else self.skeletonImage, anchor=NW)

    def moveSkeletons(self):

        skelt = self.allCharacters

        if len(self.skeletons) != 0:
            for b in range(len(skelt)):
                randomPositions = ['upward', 'downward', 'forward', 'backward']
                randomPositionsB = ['upward', 'downward', 'backward']
                randomPositionsU = ['upward', 'forward', 'backward']
                randomPositionsD = ['downward', 'forward', 'backward']

                if skelt[b]['direction'] == 'forward':
                    if skelt[b]['position'][0] < 9 and layoutArray[skelt[b]['position'][1]][skelt[b]['position'][0] + 1] == 'o':
                        skelt[b]['position'] = [skelt[b]['position']
                                                [0] + 1, skelt[b]['position'][1]]
                        if (skelt[b]['position'][1] < 9 and layoutArray[skelt[b]['position'][1] + 1][skelt[b]['position'][0]] == 'o') or (skelt[b]['position'][1] > 0 and layoutArray[skelt[b]['position'][1] - 1][skelt[b]['position'][0]] == 'o'):
                            skelt[b]['direction'] = randomPositions[randint(
                                0, 2)]
                    else:
                        skelt[b]['direction'] = randomPositions[randint(0, 1)]

                if skelt[b]['direction'] == 'backward':
                    if skelt[b]['position'][0] > 0 and layoutArray[skelt[b]['position'][1]][skelt[b]['position'][0] - 1] == 'o':
                        skelt[b]['position'] = [skelt[b]['position']
                                                [0] - 1, skelt[b]['position'][1]]
                        if (skelt[b]['position'][1] < 9 and layoutArray[skelt[b]['position'][1] + 1][skelt[b]['position'][0]] == 'o') or (skelt[b]['position'][1] > 0 and layoutArray[skelt[b]['position'][1] - 1][skelt[b]['position'][0]] == 'o'):
                            skelt[b]['direction'] = randomPositionsB[randint(
                                0, 2)]
                    else:
                        skelt[b]['direction'] = randomPositions[randint(0, 1)]

                if skelt[b]['direction'] == 'downward':
                    if skelt[b]['position'][1] < 9 and layoutArray[skelt[b]['position'][1] + 1][skelt[b]['position'][0]] == 'o':
                        skelt[b]['position'] = [skelt[b]['position']
                                                [0], skelt[b]['position'][1] + 1]
                        if (skelt[b]['position'][0] < 9 and layoutArray[skelt[b]['position'][1]][skelt[b]['position'][0] + 1] == 'o') or (skelt[b]['position'][0] > 0 and layoutArray[skelt[b]['position'][1]][skelt[b]['position'][0] - 1] == 'o'):
                            skelt[b]['direction'] = randomPositions[randint(
                                1, 3)]
                    else:
                        skelt[b]['direction'] = randomPositions[randint(2, 3)]

                if skelt[b]['direction'] == 'upward':
                    if skelt[b]['position'][1] > 0 and layoutArray[skelt[b]['position'][1] - 1][skelt[b]['position'][0]] == 'o':
                        skelt[b]['position'] = [skelt[b]['position']
                                                [0], skelt[b]['position'][1] - 1]
                        if (skelt[b]['position'][0] < 9 and layoutArray[skelt[b]['position'][1]][skelt[b]['position'][0] + 1] == 'o') or (skelt[b]['position'][0] > 0 and layoutArray[skelt[b]['position'][1]][skelt[b]['position'][0] - 1] == 'o'):
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

            # if len(self.skeletons) == 0:

    def levelUp(self):

        if self.hero.HERO_DP < 1:
            self.stats.heroKilled = True

        for i, character in enumerate(self.allCharacters):
            if character['key'] == 1:
                keyHolder = i
            if character['character'] == "Boss":
                boss = i
        if self.allCharacters[boss]['hp'] < 1 and self.allCharacters[keyHolder]['hp'] < 1:
            self.stats.levelUp()
            self.stats.levelComplete = True

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
            self.hero.heroChar['hp'] = self.hero.heroChar['hp'] - 3

            if self.allCharacters[self.skeletonStrike]["key"]:
                print(
                    f'{self.allCharacters[self.skeletonStrike]["character"]} has the key')
