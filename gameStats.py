

class Stats:
    def __init__(self):
        self.level = 1
        self.levelComplete = False
        self.heroKilled = False

    def levelUp(self):
        self.prevLevel = self.level
        self.level = self.level + 1
        print(self.level)
