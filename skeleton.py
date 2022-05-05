"""Skeleton module"""

from random import randint, sample
from default import SkeletonHealthDefault


class Skeleton(SkeletonHealthDefault):
    """Skeleton class"""

    def __init__(self, level, characters='None', tiles="None"):
        super().__init__(level)
        self.characters = characters
        self.tiles = tiles
        self.enemy = 0
        self.enemies_needed = self.characters.enemies_needed
        self.random_key = randint(0, self.characters.enemies_needed - 1)

    def create_enemies(self):
        """Creating skeleton enemies"""

        random_range_sample = sample(range(0, 10), 10)

        while self.enemy < self.enemies_needed:
            key = True if self.enemy == self.random_key else False

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
            # Creating the enemies here
            if self.tiles[random_skeleton_position[1]][random_skeleton_position[0]] == 'o':
                if not random_skeleton_position[1] == random_skeleton_position[0] == 0:
                    # Making sure the enemies don't land in the hero box
                    if not (random_skeleton_position[0] < 3 and random_skeleton_position[1] < 3):
                        self.characters.set_character(skeleton_object)
                        self.enemy += 1
