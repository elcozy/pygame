# from Layout import *
# from tkinter import *


class GameLayout():

    def __init__(self, skeletons, hero, stats):
        self.hero = hero
        self.skeletons = skeletons
        self.stats = stats
        self.max_skeleton_hp = 0

    def create_info(self, canva, bottom):
        hero_stat = self.hero
        level = self.stats.level
        canva.create_text(180, bottom + 20,  fill="darkblue", font="Times 20 italic bold",
                          text=f'Hero (Level {level}) HP: {hero_stat.hero_hp}/{hero_stat.max_hero_hp} | DP: {hero_stat.hero_dp} | SP: {hero_stat.hero_sp}')
        # print('My health == here')

    def create_info_enemy(self, canva, bottom, char):
        self.max_skeleton_hp = self.skeletons.all_characters[char]['hp']

        enemy_stat = self.skeletons.all_characters[char]
        level = self.stats.level
        canva.create_text(180, bottom + 40,  fill="darkblue", font="Times 20 italic bold",
                          text=f'{enemy_stat["character"]} (Level {level}) HP: {enemy_stat["hp"]}/{self.max_skeleton_hp} | DP: {enemy_stat["dp"]} | SP: {enemy_stat["sp"]}')
