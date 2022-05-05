"""Hero module"""
from tkinter import PhotoImage, NW
from game_constants import IMG_SIZE, FILEPATH
from default import HeroHealthDefault


class Hero(HeroHealthDefault):
    """The class for the hero"""

    def __init__(self, level, tiles='None'):
        super().__init__()
        self.level = level
        self.tiles = tiles
        self.hero_position = [0, 0]
        self.move_time = 1
        self.hero_strike = ''

    def create_hero(self, canva):
        """Creating the hero canvas"""
        i = self.hero_position[0] * IMG_SIZE
        j = self.hero_position[1] * IMG_SIZE

        if self.hero_hp > 0:
            canva.create_image(
                i, j, image=self.heroface, anchor=NW)
        else:
            self.hero_position = [-1, -1]

    def move_hero(self, img, i=0, j=0):
        """Moving the Hero"""
        self.img = img
        self.heroface = PhotoImage(
            file=f"{FILEPATH}{img}.png")

        x_pos = self.hero_position[0]
        y_pos = self.hero_position[1]

        if i and self.tiles[y_pos][x_pos + i] == 'o':
            self.hero_position = [x_pos + i, y_pos]

        if j and self.tiles[y_pos + j][x_pos] == 'o':
            self.hero_position = [x_pos, y_pos + j]
        self.move_time += 1

        if self.move_time == 3:
            self.move_time = 1

    def strike_enemy(self, skeleton):
        """Enemy strike method"""

        for character in (skeleton.all_characters):
            if character["position"] == self.hero_position:
                if character['hp'] > 0:
                    character['hp'] = character['hp'] - 5
                else:
                    character['hp'] = 0
