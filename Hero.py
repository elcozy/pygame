from Layout import layoutArray
from time import time, sleep


class Hero:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.img = "hero_down"

    def move(self, img, x=0, y=0):
        self.img = img
        if x and layoutArray[self.y][self.x + x] is 'o':
            self.x += x

        if y and layoutArray[self.y + y][self.x] is 'o':
            # while y:
            self.y += y

        print(self.x, self.y)
