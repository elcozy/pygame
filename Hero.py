from Layout import *


class Hero:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.img = "hero_down"

    def move(self, img, x=0, y=0):
        self.img = img
        print(layoutArray[self.y][self.x], '----', 'x:', x, 'y:', y)

        if x == 1 and layoutArray[self.y][self.x + 1] is 'o':
            self.x += x

        if x == -1 and layoutArray[self.y][self.x - 1] is 'o':
            self.x += x

        if y == 1 and layoutArray[self.y + 1][self.x] is 'o':
            self.y += y
        if y == -1 and layoutArray[self.y - 1][self.x] is 'o':
            self.y += y

        print(self.x, self.y)
