from time import time, sleep
from random import randint
from maps import tiles


class Boss:

    def __init__(self):
        self.x = randint(0, 9)
        self.y = randint(0, 9)

    def checkPosition(self):
        layoutArray = tiles

        while layoutArray[self.y][self.x] is 'x':
            self.x = randint(0, 9)
            self.y = randint(0, 9)
