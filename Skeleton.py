
from random import randint, sample
import numpy as np
from tkinter import *
from hero import Hero
from random_character import Random
from maps import tiles
import time


IMG_SIZE = 72
WIDTH = 10 * IMG_SIZE
HEIGHT = 10 * IMG_SIZE

filePath = 'assets/img/'
layoutArray = tiles


class CharactersHealthDefault():
    def __init__(self):
        self.level = 1
        self.HP = (2 * self.level) * randint(1, 6)
        self.DP = (self.level / 2) * randint(1, 6)
        self.SP = self.level * randint(1, 6)
        self.BOSS_HP = (2 * self.level) * (randint(1, 6) + randint(1, 6))
        self.BOSS_DP = (self.level / 2) * (randint(1, 6) + (randint(1, 6) / 2))
        self.BOSS_SP = self.level * randint(1, 6) + self.level
        self.bossImage = PhotoImage(file=f"{filePath}boss.png")
        self.skeletonImage = PhotoImage(file=f"{filePath}skeleton.png")


class Skeletons(CharactersHealthDefault):

    def __init__(self, skeletonsNeeded=3):
        super().__init__()
        self.skeletons = []
        self.allCharacters = []
        self.bossPosition = [0, 0]
        self.enemy = 1
        self.enemiesNeeded = skeletonsNeeded

    def setEnemy(self, character, position, enemyCount=1):
        if character == 'boss':
            return {
                "character": f"Boss",
                'direction': 'forward',
                "position": position,
                'hp': self.HP,
                'dp': self.DP,
                'sp': self.SP
            }
        if character == 'skeleton':
            return {
                "character": f"{character}{enemyCount}",
                'direction': 'forward',
                'key': FALSE,
                "position": position,
                'hp': self.BOSS_HP,
                'dp': self.BOSS_DP,
                'sp': self.BOSS_SP
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
            skeletonObject = Skeletons().setEnemy('skeleton', randomArr, self.enemy)
            bossObject = Skeletons().setEnemy('boss', randomArrBoss)
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
            x = self.allCharacters[i]['position'][0] * IMG_SIZE
            y = self.allCharacters[i]['position'][1] * IMG_SIZE

            if i < len(self.skeletons) - 1:
                canva.create_image(
                    x, y, image=self.skeletonImage, anchor=NW)
            else:
                canva.create_image(x, y, image=self.bossImage, anchor=NW)

        # if len(self.skeletons) != 0:
        #     Skeletons().checkWallBlock(0, x=1)

    def checkWallBlock(self, char, x=0, y=0):
        print('block')
        # if x:
        #     if layoutArray[self.skeletons[char][1]][self.skeletons[char][0]] == 'x':
        #         print('next is wall')
        # if y:
        #     if layoutArray[self.skeletons[char][1] + y][self.skeletons[char][0] + x] == 'x':
        #         print('next is wall')

    def moveSkeletons(self):
        # time.sleep(2)
        skelt = self.allCharacters

        if len(skelt) != 0:
            # print(skelt, 'skeletons')
            for b in range(len(skelt)):
                randomPositions = ['upward', 'downward', 'forward', 'backward']

                # if layoutArray[skeletonObjectPosition[1]][skeletonObjectPosition[0]] == 'o'

                if skelt[b]['direction'] == 'forward':
                    # if skelt[b]['position'][0] < 9:
                    if skelt[b]['position'][0] < 9 and layoutArray[skelt[b]['position'][1]][skelt[b]['position'][0] + 1] == 'o':
                        skelt[b]['position'] = [skelt[b]['position']
                                                [0] + 1, skelt[b]['position'][1]]

                    else:
                        skelt[b]['direction'] = 'downward'

                if skelt[b]['direction'] == 'backward':
                    # if skelt[b]['position'][0] > 0:
                    if skelt[b]['position'][0] > 0 and layoutArray[skelt[b]['position'][1]][skelt[b]['position'][0] - 1] == 'o':
                        skelt[b]['position'] = [skelt[b]['position']
                                                [0] - 1, skelt[b]['position'][1]]
                    else:
                        skelt[b]['direction'] = 'upward'

                if skelt[b]['direction'] == 'downward':
                    # if skelt[b]['position'][0] > 0:
                    if skelt[b]['position'][1] < 9 and layoutArray[skelt[b]['position'][1] + 1][skelt[b]['position'][0]] == 'o':
                        skelt[b]['position'] = [skelt[b]['position']
                                                [0], skelt[b]['position'][1] + 1]
                    else:
                        skelt[b]['direction'] = 'backward'

                if skelt[b]['direction'] == 'upward':
                    # if skelt[b]['position'][0] < 9:
                    if skelt[b]['position'][1] > 0 and layoutArray[skelt[b]['position'][1] - 1][skelt[b]['position'][0]] == 'o':
                        skelt[b]['position'] = [skelt[b]['position']
                                                [0], skelt[b]['position'][1] - 1]
                    else:
                        # if skelt[b]['position'][0] == 9:
                        skelt[b]['direction'] = 'forward'
                print('-------------')
                print(skelt[b]['direction'], skelt[b]
                      ['character'], skelt[b]['position'][0])

        # print(xPos, ':xPosition')
        # print(yPos, ':yPosition')

        # if self.movex1:
        #     if self.direction1 == 1 and (wallRight or xds[1]):
        #         self.allowForward1 = False
        #         self.x1direction = 0
        #         print('wall found to the right')
        #         self.movex1 = False

        #     if self.direction1 == 0 and (wallLeft or xds[0]):
        #         self.allowForward1 = True
        #         self.x1direction = 1
        #         print('wall found to the left')
        #         self.movex1 = False
        #     skeleton.moveSkeletons()
        # if self.allowForward1 == True and (wallRight) == False:
        #     # self.forwardx1 = False
        #     self.x1 += 1
        # if self.allowForward1:
        #     self.x1x1direction -= 1
        # # self.forwardx1 = True


class SkeletonMovement(Skeletons):

    def __init__(self):
        super().__init__()
        self.x1 = 4
        self.y1 = 5

        self.x1direction = 1
        # self.x1direction = randint(0, 1)
        self.movex1 = True
        self.forwardx1 = True
        self.allowForward1 = True
        self.allowDownward1 = False if self.y1 < 9 else True
        self.forwardy1 = True

        self.direction1 = None

    def blockWalls(self, x=0, y=0):
        isRightTileWall = True
        isLeftTileWall = True
        isDownTileWall = True
        isUpTileWall = True
        if x == 1:
            if x < len(layoutArray[self.y1]) - 1:
                isRightTileWall = layoutArray[self.y1][self.x1 + 1] == 'x'
            if x > 0:
                isLeftTileWall = layoutArray[self.y1][self.x1 - 1] == 'x'
            return [isLeftTileWall, isRightTileWall]

        if y == 1:
            if self.y1 < len(layoutArray) - 1:
                isDownTileWall = layoutArray[self.y1 + 1][self.x1] == 'x'
            if self.y1 > 0:
                isUpTileWall = layoutArray[self.y1 - 1][self.x1] == 'x'
            return [isUpTileWall, isDownTileWall]

    def moveSkeletons(self):

        xPos = self.skeletons[0][0]
        yPos = self.skeletons[0][1]

        wallLeft = self.x1 == 0
        wallRight = self.x1 == 9
        # print(self.x1, self.y1, '1 position')
        allowForward1 = self.allowForward1

        gameDirections = ['Left', "Right", 'Up', 'Down']

        # time.sleep(1)

        print((wallRight),
              self.direction1, allowForward1)
        print((wallLeft),
              self.direction1, allowForward1)
        skeleton = SkeletonMovement()
        xds = skeleton.blockWalls(x=self.x1direction)
        print('blok', xds, self.allowForward1)

        if self.movex1:
            if self.direction1 == 1 and (wallRight or xds[1]):
                self.allowForward1 = False
                self.x1direction = 0
                print('wall found to the right')
                self.movex1 = False

            if self.direction1 == 0 and (wallLeft or xds[0]):
                self.allowForward1 = True
                self.x1direction = 1
                print('wall found to the left')
                self.movex1 = False
            skeleton.moveSkeletons()
            # if self.allowForward1 == True and (wallRight) == False:
            #     # self.forwardx1 = False
            #     self.x1 += 1
            # if self.allowForward1:
            #     self.x1x1direction -= 1
            # # self.forwardx1 = True
