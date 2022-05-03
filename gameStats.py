

class Stats():
    def __init__(self):
        self.level = 1
        self.level_complete = False
        self.hero_killed = False

    def levelUp(self):
        self.level = self.level + 1
