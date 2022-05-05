"""Map module"""
from tkinter import PhotoImage
import random
from game_constants import IMG_SIZE, FILEPATH


tiles = []

with open('tiles.txt', 'r', encoding="utf-8") as file:
    tile_file = file.readlines()

for line in tile_file:
    tiles.append(line)


class MapTiles:
    """"Class for map tiles"""

    def __init__(self):
        self.level = 1
        self.tiles = tiles

        self.tile_open = PhotoImage(
            file=f"{FILEPATH}floor.png")

        self.tile_block = PhotoImage(
            file=f"{FILEPATH}wall.png")

    def shuffle_tiles(self):
        """"Shuffling tiles"""
        return random.shuffle(self.tiles)

    def draw_tiles(self, canva):
        """Method for drawing tiles"""
        tile_row = 0

        for index, block in enumerate(self.tiles):
            for i in range(len(block) - 1):
                canvas_image = self.tile_open if block[i] == 'o' else self.tile_block
                canva.create_image(i * IMG_SIZE, tile_row *
                                   IMG_SIZE, image=canvas_image, anchor='nw')
            if index == len(self.tiles) - 1:
                break
            tile_row += 1
