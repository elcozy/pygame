
from random import randint
import numpy as np
from tkinter import *
from hero import Hero
from random_character import Random
from maps import tiles

IMG_SIZE = 72
WIDTH = 10 * IMG_SIZE
HEIGHT = 10 * IMG_SIZE

filePath = 'assets/img/'
layoutArray = tiles


class Skeletons(Hero):

    def __init__(self):
        # super().__init__(filePath)
        self.skeletons = []
        self.diffEnemiesLocation = False
        self.skeleton = PhotoImage(file=f"{filePath}skeleton.png")
        self.skeletn1Good = False
        self.skeletn2Good = False
        self.skeletn3Good = False
        self.boss = PhotoImage(file=f"{filePath}boss.png")
        self.bossPosition = [0, 0]
        self.bossGood = False
        self.level = 1

    def createEnemies(self, canva):
        emptyArr = [0, 0]
        skeletn1 = emptyArr
        skeletn2 = emptyArr
        skeletn3 = emptyArr
        boss = [0, 0]
        for i in range(len(self.skeletons)):
            x = self.skeletons[i][0] * IMG_SIZE
            y = self.skeletons[i][1] * IMG_SIZE
            canva.create_image(
                x, y, image=self.skeleton, anchor=NW)
        canva.create_image(self.bossPosition[0] * IMG_SIZE, self.bossPosition[1] *
                           IMG_SIZE, image=self.boss, anchor=NW)
        # for enem in enemiesBoss:

        while not self.diffEnemiesLocation:

            if not self.skeletn1Good and layoutArray[skeletn1[1]][skeletn1[0]] == 'o' and not (skeletn1[1] == skeletn1[0] == 0):
                skeletn1 = skeletn1
                self.skeletn1Good = True
                print('sk1 is good')
                self.skeletons.append(skeletn1)
            else:
                skeletn1 = [randint(0, 9), randint(0, 9)]
            if not self.skeletn2Good and layoutArray[skeletn2[1]][skeletn2[0]] == 'o' and not (skeletn2[1] == skeletn2[0] == 0):
                skeletn2 = skeletn2
                self.skeletn2Good = True
                print('sk2 is good')
                self.skeletons.append(skeletn2)
            else:
                skeletn2 = [randint(0, 9), randint(0, 9)]
            if not self.skeletn3Good and layoutArray[skeletn3[1]][skeletn3[0]] == 'o' and not (skeletn3[1] == skeletn3[0] == 0):
                skeletn3 = skeletn3
                print('sk3 is good')
                self.skeletn3Good = True
                self.skeletons.append(skeletn3)
            else:
                skeletn3 = [randint(0, 9), randint(0, 9)]
            if not self.bossGood and layoutArray[boss[1]][boss[0]] == 'o' and not (boss[1] == boss[0] == 0):
                self.bossPosition = boss
                print('sk3 is good')
                self.bossGood = True
            else:
                boss = [randint(0, 9), randint(0, 9)]

            print(self.skeletons, 'array', self.boss)
            allSkelGood = (
                self.skeletn1Good and self.skeletn2Good and self.skeletn3Good and self.bossGood)
            skelSimilar = (np.array_equal(skeletn1, skeletn2)
                           and np.array_equal(skeletn2, skeletn3) and (skeletn3, self.bossPosition))

            if not self.diffEnemiesLocation and allSkelGood and not skelSimilar:
                print('All skeleton locations are different')
                self.diffEnemiesLocation = True
                break


class MonsterLevel(Skeletons):
    def __init__(self):
        super().__init__()
        self.skeletons = self.skeletons
        self.skeleton1 = Random.randomInt()
        self.skeleton2 = Random.randomInt()
        self.skeleton3 = Random.randomInt()
        self.HP = 2 * self.level * randint(1, 6)
        self.DP = self.level / 2 * randint(1, 6)
        self.SP = self.level * randint(1, 6)

    def checkSkeletons(self):
        print(self.skeletons, 'checking')


class Skeleton():

    def __init__(self):
        self.x1 = 4
        self.y1 = 5
        self.x2 = randint(0, 9)
        self.y2 = randint(0, 9)
        self.x3 = randint(0, 9)
        self.y3 = randint(0, 9)
        self.x1direction = 1
        # self.x1direction = randint(0, 1)
        self.movex1 = True
        self.forwardx1 = True
        self.allowForward1 = True
        self.allowDownward1 = False if self.y1 < 9 else True
        self.forwardy1 = True

        self.direction1 = None

    def checkPosition(self, x=0, y=0):
        while layoutArray[self.y1][self.x1] == 'x' or self.x1 == self.y1 == 0:
            self.x1 = randint(0, 9)
            self.y2 = randint(0, 9)
        while layoutArray[self.y2][self.x2] == 'x' or self.x2 == self.y2 == 0:
            self.x2 = randint(0, 9)
            self.y2 = randint(0, 9)
        while layoutArray[self.y3][self.x3] == 'x' or self.x3 == self.y3 == 0:
            self.x3 = randint(0, 9)
            self.y3 = randint(0, 9)

        print(self.x1, self.y1, 'self1')
        # print(self.x2, self.y2, 'self2')
        # print(self.x3, self.y3, 'self3')

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

    def moveSkeleton(self):
        skeleton = Skeleton()
        xds = skeleton.blockWalls(x=self.x1direction)
        print('blok', xds, self.allowForward1)
        if self.allowForward1 == True and not xds[1]:
            # self.forwardx1 = False
            print('I soukd go front')
            self.x1 += 1
        else:
            self.x1 -= 1
        # if self.allowForward1:
        #     self.x1x1direction -= 1
        # self.forwardx1 = True

    def moveSkeletons(self):
        wallLeft = self.x1 == 0
        wallRight = self.x1 == 9
        allowForward1 = self.allowForward1

        gameDirections = ['Left', "Right", 'Up', 'Down']

        time.sleep(1)

        print((wallRight),
              self.direction1, allowForward1)
        print((wallLeft),
              self.direction1, allowForward1)
        skeleton = Skeleton()
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
            skeleton.moveSkeleton()
            # if self.allowForward1 == True and (wallRight) == False:
            #     # self.forwardx1 = False
            #     self.x1 += 1
            # if self.allowForward1:
            #     self.x1x1direction -= 1
            # # self.forwardx1 = True

        if not self.movex1:
            print('y axiz now')
        #     print("x should move now")
        #     if self.x1direction == 'Down' and (wallDown or isDownTileWall):
        #         self.allowDownward1 = False
        #         print('wall found down')
        #         # self.movey1 = False

        #     if self.x1direction == 'Up' and (wallUp or isUpTileWall):
        #         self.allowDownward1 = True
        #         print('wall found up')
        #         # self.movey1 = False
        #     print('wall forwardy1:', self.allowDownward1)

        #     if self.allowDownward1 and self.y1 < 10:
        #         # self.forwardy1 = False
        #         self.y1 += 1
        #     if self.allowDownward1 and self.y1 > 0:
        #         self.y1 -= 1
        #         # self.forwardy1 = True

        print('x1 :', self.x1)

        # if layoutArray[self.y1][self.x1 + 1] == 'x':
        #     self.x1 -= 1
        #     self.allowForwardx1 = False
        print(self.x1)
