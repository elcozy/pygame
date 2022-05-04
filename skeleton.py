from random import randint, sample
from default import SkeletonHealthDefault


class Skeleton(SkeletonHealthDefault):
    """Skeleton class"""

    def __init__(self, level, characters='None', tiles="None"):
        super().__init__(level)
        self.characters = characters
        self.tiles = tiles
        self.enemy = 0
        self.enemies_needed = self.characters.enemiesNeeded
        self.random_key = randint(0, self.characters.enemiesNeeded - 1)

    def create_enemies(self):
        """Creating skeleton enemies"""
        # Generating random number from 0 - 10
        key = True if self.enemy is self.random_key else False
        print(key)
        random_range_sample = sample(range(0, 10), 10)

        while self.enemy < self.enemies_needed:
            key = True if self.enemy is self.random_key else False
            print(key)
            # Assigning to variables here
            random_skeleton_position = [
                random_range_sample[self.enemy], randint(0, 9)]

            skeleton_object = {
                "character": f"Skeleton{self.enemy}",
                'direction': 'forward',
                'key': key,
                "position": random_skeleton_position,
                'hp': self.skeleton_hp,
                'dp': self.skeleton_dp,
                'sp': self.skeleton_sp
            }
            print(self.tiles, 'tiles in SKel')
            # Creating the enemies here
            if self.tiles[random_skeleton_position[1]][random_skeleton_position[0]] is 'o':
                if not (random_skeleton_position[1] is random_skeleton_position[0] is 0):
                    # Making sure the enemies don't land in the hero box
                    if not (random_skeleton_position[0] < 3 and random_skeleton_position[1] < 3):
                        self.characters.setCharacter(skeleton_object)
                        self.enemy += 1
