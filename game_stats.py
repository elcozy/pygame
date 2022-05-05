""""Module for stats management"""


class Stats():
    """"stats class"""

    def __init__(self):
        self.level = 1
        self.level_complete = False
        self.hero_killed = False

    def level_up_stats(self):
        """Level up module"""
        self.level = self.level + 1
