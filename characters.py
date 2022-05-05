"""Characters module"""

from random import randint
import time
from tkinter import PhotoImage, NW
from game_constants import IMG_SIZE, FILEPATH


class MainCharacter():
    """The main characters class"""
    last_move_time = time.time()

    def __init__(
            self,
            hero='None',
            stats='None',
            tiles=None,
            skeletons_needed=3):

        self.stats = stats
        self.hero = hero
        self.tiles = tiles
        self.skeletons = []
        self.all_characters = []
        self.enemy = 1
        self.enemies_needed = skeletons_needed
        self.skeleton_strike = ''
        self.rand_key = randint(0, self.enemies_needed - 1)
        self.skeleton_image = PhotoImage(
            file=f"{FILEPATH}skeleton.png")
        self.boss_img = PhotoImage(file=f"{FILEPATH}boss.png")

    def set_character(self, character):
        """Setter for the characters"""
        self.all_characters.append(character)

    def create_enemies(self, canva):
        """Creating the enemies"""

        # for i, j in enumerate(self.all_characters):
        for character in self.all_characters:
            x_pos = character['position'][0] * IMG_SIZE
            y_pos = character['position'][1] * IMG_SIZE

            if character['hp'] > 0:
                character_name = character['character']
                canva.create_image(
                    x_pos,
                    y_pos,
                    image=self.boss_img if character_name == 'Boss' else self.skeleton_image,
                    anchor=NW)

    def move_skeletons(self):
        """Moving all skeletons"""

        self.all_characters = self.all_characters

        if len(self.skeletons) != 0:
            for j in enumerate(self.all_characters):
                i = j[0]

                rand_pos = ['upward', 'downward', 'forward', 'backward']
                rand_pos_b = ['upward', 'downward', 'backward']
                rand_pos_u = ['upward', 'forward', 'backward']

                character_x_pos = self.all_characters[i]['position'][0]
                character_y_pos = self.all_characters[i]['position'][1]

                x_next_tile_valid = character_x_pos < 9 and self.tiles[
                    character_y_pos][character_x_pos + 1] == 'o'
                y_next_tile_valid = character_y_pos < 9 and self.tiles[
                    character_y_pos + 1][character_x_pos] == 'o'

                x_prev_tiles_valid = character_x_pos > 0 and self.tiles[
                    character_y_pos][character_x_pos - 1] == 'o'
                y_prev_tiles_valid = character_y_pos > 0 and self.tiles[
                    character_y_pos - 1][character_x_pos] == 'o'

                if self.all_characters[i]['direction'] == 'forward':
                    if x_next_tile_valid:
                        self.all_characters[i]['position'] = [
                            character_x_pos + 1, character_y_pos]

                        character_x_pos = self.all_characters[i]['position'][0]

                        y_next_tile_valid = character_y_pos < 9 and self.tiles[
                            character_y_pos + 1][character_x_pos] == 'o'
                        y_prev_tiles_valid = character_y_pos > 0 and self.tiles[
                            character_y_pos - 1][character_x_pos] == 'o'

                        if y_next_tile_valid or y_prev_tiles_valid:
                            self.all_characters[i]['direction'] = rand_pos[randint(
                                0, 2)]
                    else:
                        self.all_characters[i]['direction'] = rand_pos[randint(
                            0, 1)]

                if self.all_characters[i]['direction'] == 'backward':
                    if x_prev_tiles_valid:
                        self.all_characters[i]['position'] = [
                            character_x_pos - 1, character_y_pos]
                        character_x_pos = self.all_characters[i]['position'][0]

                        y_next_tile_valid = character_y_pos < 9 and self.tiles[
                            character_y_pos + 1][character_x_pos] == 'o'
                        y_prev_tiles_valid = character_y_pos > 0 and self.tiles[
                            character_y_pos - 1][character_x_pos] == 'o'

                        if y_next_tile_valid or y_prev_tiles_valid:
                            self.all_characters[i]['direction'] = rand_pos_b[randint(
                                0, 2)]
                    else:
                        self.all_characters[i]['direction'] = rand_pos[randint(
                            0, 1)]

                if self.all_characters[i]['direction'] == 'downward':
                    if y_next_tile_valid:
                        self.all_characters[i]['position'] = [
                            character_x_pos, character_y_pos + 1]

                        character_y_pos = self.all_characters[i]['position'][1]
                        x_next_tile_valid = character_x_pos < 9 and self.tiles[
                            character_y_pos][character_x_pos + 1] == 'o'
                        x_prev_tiles_valid = character_x_pos > 0 and self.tiles[
                            character_y_pos][character_x_pos - 1] == 'o'

                        if x_next_tile_valid or x_prev_tiles_valid:
                            self.all_characters[i]['direction'] = rand_pos[randint(
                                1, 3)]
                    else:
                        self.all_characters[i]['direction'] = rand_pos[randint(
                            2, 3)]

                if self.all_characters[i]['direction'] == 'upward':
                    if y_prev_tiles_valid:
                        self.all_characters[i]['position'] = [
                            character_x_pos, character_y_pos - 1]

                        character_y_pos = self.all_characters[i]['position'][1]
                        x_next_tile_valid = character_x_pos < 9 and self.tiles[
                            character_y_pos][character_x_pos + 1] == 'o'
                        x_prev_tiles_valid = character_x_pos > 0 and self.tiles[
                            character_y_pos][character_x_pos - 1] == 'o'

                        if x_next_tile_valid or x_prev_tiles_valid:
                            self.all_characters[i]['direction'] = rand_pos_u[randint(
                                0, 2)]
                    else:
                        self.all_characters[i]['direction'] = rand_pos[randint(
                            2, 3)]

    def next_direction(self, direction):
        """NExt direction for the skeleton"""
        if direction == 'forward':
            pass

    def update_skeletons(self):
        """Updating skeletons"""
        self.skeletons = []
        for character in self.all_characters:
            if character['hp'] > 0:
                self.skeletons.append(
                    character['position'])

            # if len(self.skeletons) == 0:

    def level_up(self):
        """levelling up"""
        if self.hero.hero_hp < 1:
            self.stats.hero_life(True)
        if len(self.all_characters) > 0:
            for i, character in enumerate(self.all_characters):
                if character['key'] is True:
                    key_holder = i
                if character['character'] == "Boss":
                    boss = i

            if self.all_characters[boss]['hp'] < 1 and self.all_characters[key_holder]['hp'] < 1:
                print('boss and key holder killed')
                self.stats.level_up_stats()
                self.stats.level_complete = True

    def strike_hero(self):
        """Striking hero"""
        hero_pos = self.hero.hero_position

        if hero_pos in self.skeletons:
            self.skeleton_strike = self.skeletons.index(hero_pos)
        else:
            self.skeleton_strike = ''

        if time.time() - self.last_move_time < 1:
            return
        self.last_move_time = time.time()

        if self.skeleton_strike != '':
            self.skeleton_strike = self.skeletons.index(hero_pos)
            self.hero.hero_hp = self.hero.hero_hp - 3

            if self.all_characters[self.skeleton_strike]["key"]:
                print(
                    f'{self.all_characters[self.skeleton_strike]["character"]} has the key')
