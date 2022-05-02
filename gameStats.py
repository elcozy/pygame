

class Stats:
    def __init__(self, level=1):
        self.level = level

    def levelUp(self):
        self.level + 1

    def gameOver(self):
        self.level = 0
