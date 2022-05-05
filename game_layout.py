

class GameLayout():

    def __init__(self, skeletons, hero, stats):
        self.hero = hero
        self.skeletons = skeletons
        self.stats = stats

    def create_info(self, canva, bottom):
        """Cretaing hero for hero"""
        hero_stat = self.hero
        level = self.stats.level
        hero_stat = f'Hero (Level {level}) HP: {hero_stat.hero_hp}/{hero_stat.max_hero_hp} | DP: {hero_stat.hero_dp} | SP: {hero_stat.hero_sp}'
        canva.create_text(180, bottom + 20,  fill="darkblue",
                          font="Times 20 italic bold", text=hero_stat)

    def create_info_enemy(self, canva, bottom, char):
        """Creating info for ememies"""
        enemy_stat = self.skeletons.all_characters[char]
        info_stat = f'{enemy_stat["character"]}  HP: {enemy_stat["hp"]} | DP: {enemy_stat["dp"]} | SP: {enemy_stat["sp"]}'
        canva.create_text(195, bottom + 40,  fill="darkblue",
                          font="Times 20 italic bold", text=info_stat)
