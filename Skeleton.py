from Layout import layoutArray
from time import time, sleep


class Skeleton:

    def __init__(self):
        self.x = 2
        self.y = 1

    def start(self, x=0, y=0):
        print(layoutArray[self.y][self.x], '----', 'x:', x, 'y:', y)

        if x and layoutArray[self.y][self.x + x] is 'o':
            self.x += x

        if y and layoutArray[self.y + y][self.x] is 'o':
            # while y:
            self.y += y

        print(self.x, self.y)
