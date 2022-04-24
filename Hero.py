from maps import tiles
import random
import numpy as np
from tkinter import *


class Hero():

    def __init__(self, filePath):
        self.filePath = filePath
        self.x = 0
        self.y = 0
        self.hero_position = [0, 0]
        self.level = 1
        self.img = "hero-down"
        self.heroface = PhotoImage(file=f"{self.filePath}{self.img}.png")

    def createHero(self, canva, IMG_SIZE):
        x = self.x * IMG_SIZE
        y = self.y * IMG_SIZE
        x_pos = self.hero_position[0] * IMG_SIZE
        y_pos = self.hero_position[1] * IMG_SIZE
        canva.create_image(x_pos, y_pos, image=self.heroface, anchor=NW)
        # canva.create_image(x, y, image=self.heroface, anchor=NW)

    def move(self, img, x=0, y=0):
        layoutArray = tiles
        self.img = img
        xs = self.hero_position[0]
        ys = self.hero_position[1]

        if x and layoutArray[ys][xs + x] == 'o':
            # if x and layoutArray[self.y][self.x + x] == 'o':

            # self.x += x
            self.hero_position = [xs + x, ys]

        if y and layoutArray[ys + y][xs] == 'o':
            # if y and layoutArray[self.y + y][self.x] == 'o':
            # while y:
            # self.y += y

            # self.x += x
            self.hero_position = [xs, ys + y]
        print(self.hero_position)
