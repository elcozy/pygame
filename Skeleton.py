
from random import randint, sample
import numpy as np
from tkinter import *
from random_character import Random
from maps import tiles
import time

layoutArray = tiles


class CharactersHealthDefault():
    def __init__(self, FILEPATH):
        self.level = 1
        self.SKELETON_HP = (2 * self.level) * randint(1, 6)
        self.SKELETON_DP = (self.level / 2) * randint(1, 6)
        self.SKELETON_SP = self.level * randint(1, 6)
        self.BOSS_HP = (2 * self.level) * (randint(1, 6) + randint(1, 6))
        self.BOSS_DP = (self.level / 2) * (randint(1, 6) + (randint(1, 6) / 2))
        self.BOSS_SP = self.level * randint(1, 6) + self.level
        self.bossImage = PhotoImage(file=f"{FILEPATH}boss.png")
        self.skeletonImage = PhotoImage(
            file=f"{FILEPATH}skeleton.png")


class Skeletons(CharactersHealthDefault):
    last_move_time = time.time()

    def __init__(self, IMG_SIZE, FILEPATH, hero=None, skeletonsNeeded=3):
        super().__init__(FILEPATH)
        self.hero = hero
        self.IMG_SIZE = IMG_SIZE
        self.skeletons = []
        self.allCharacters = []
        self.enemy = 1
        self.enemiesNeeded = skeletonsNeeded
        self.skeletonStrike = ''

    def setEnemy(self, character, position, enemyCount=1):
        if character == 'boss':
            return {
                "character": f"Boss",
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
                'key': FALSE,
                "position": position,
                'hp': self.SKELETON_HP,
                'dp': self.SKELETON_DP,
                'sp': self.SKELETON_SP
            }
        else:
            print("No enemy here")

    def createEnemies(self, canva):

        # Generating Random number from 0 - 10
        xRand = sample(range(0, 10), 10)
        while self.enemy < self.enemiesNeeded + 2:

            # Assigning to variables here
            randomArr = [xRand[self.enemy], randint(0, 9)]
            randomArrBoss = [xRand[self.enemy], randint(0, 9)]
            skeletonObject = Skeletons(self.IMG_SIZE, self.hero.FILEPATH).setEnemy(
                'skeleton', randomArr, self.enemy)
            bossObject = Skeletons(self.IMG_SIZE, self.hero.FILEPATH).setEnemy(
                'boss', randomArrBoss)
            bossObjectPosition = bossObject['position']
            skeletonObjectPosition = skeletonObject['position']

            # Creating the enemies here
            if self.enemy < self.enemiesNeeded + 1:
                if layoutArray[skeletonObjectPosition[1]][skeletonObjectPosition[0]] == 'o':
                    if not (skeletonObjectPosition[1] == skeletonObjectPosition[0] == 0):
                        # Making sure the enemies don't land in the hero box
                        if not (skeletonObjectPosition[0] < 3 and skeletonObjectPosition[1] < 3):
                            self.allCharacters.append(skeletonObject)
                            self.enemy += 1

            # Creating a boss here
            if self.enemy == self.enemiesNeeded + 1:
                if layoutArray[bossObjectPosition[1]][bossObjectPosition[0]] == 'o':
                    if not (bossObjectPosition[1] == bossObjectPosition[0] == 0):
                        # Making sure the enemies don't land in the hero box
                        if not (bossObjectPosition[0] < 3 and bossObjectPosition[1] < 3):
                            self.allCharacters.append(bossObject)

                            for z in self.allCharacters:
                                print(z)
                                pass
                                self.skeletons.append(
                                    z['position'])

                            # give random enemy key
                            keyRandom = randint(0, self.enemiesNeeded - 1)
                            self.allCharacters[keyRandom]['key'] = TRUE

                            self.enemy += 1
                            print(self.skeletons, ' characters')
                            print(self.allCharacters[1]
                                  ['position'], ' characters')

        for i in range(len(self.skeletons)):
            x = self.allCharacters[i]['position'][0] * self.IMG_SIZE
            y = self.allCharacters[i]['position'][1] * self.IMG_SIZE

            if self.allCharacters[i]['hp'] > 0:
                if i < len(self.skeletons) - 1:
                    canva.create_image(
                        x, y, image=self.skeletonImage, anchor=NW)
                else:
                    canva.create_image(x, y, image=self.bossImage, anchor=NW)

        # if len(self.skeletons) != 0:
        #     Skeletons().checkWallBlock(0, x=1)

    def moveSkeletons(self):
        print('moveSkeleton')
        # if time.time() - self.last_move_time < 1:
        #     return
        # self.last_move_time = time.time()
        # time.sleep(2)
        skelt = self.allCharacters

        if len(skelt) != 0:
            # print(skelt, 'skeletons')
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
                self.skeletons = []
                for z in self.allCharacters:
                    pass
                    self.skeletons.append(
                        z['position'])

    def getCurrentSkeleton(self, hero):
        heroArr = hero.hero_position

        if heroArr in self.skeletons:
            self.skeletonStrike = self.skeletons.index(heroArr)
        else:
            self.skeletonStrike = ''

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
            hero.HP = hero.HP - 5

            print(
                f'char strike {self.allCharacters[self.skeletonStrike]["character"]}')
            if self.allCharacters[self.skeletonStrike]["key"]:
                print(
                    f'{self.allCharacters[self.skeletonStrike]["character"]} has the key')

    def updateCharacterScore(self, index=0):
        if index:
            print(
                f'Removed 5 from {self.allCharacters[index]["character"]} HP')
            self.allCharacters[index]['hp'] = self.allCharacters[index]['hp'] - 5
        else:
            print('You need to pass an index to this method')
