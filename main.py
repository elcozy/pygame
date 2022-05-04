from tkinter import Tk, Canvas
from random import randint
from game_constants import WIDTH, HEIGHT
from hero import Hero
from characters import CharacterMain
from boss import Boss
from skeleton import Skeleton
from maps import MapTiles
from game_stats import Stats
from game_layout import GameLayout


tk = Tk()
tk.title('Wanderer Game')
canvas = Canvas(tk, width=WIDTH, height=HEIGHT + 150, bg='white')
canvas.pack()


STATS = Stats()

MAP_TILES = MapTiles()

TILES = MAP_TILES.tiles

HERO = Hero(STATS.level, TILES)


CHARACTER_MAIN = CharacterMain(HERO, STATS.level, STATS, TILES)

BOSS_INSTANCE = Boss(STATS.level, CHARACTER_MAIN, TILES)
BOSS_INSTANCE.create_enemies()

SKELETON_INSTANCE = Skeleton(STATS.level, CHARACTER_MAIN, TILES)
SKELETON_INSTANCE.create_enemies()

GAME_LAYOUT = GameLayout(CHARACTER_MAIN, HERO, STATS)

# This method is called continuously by the main game loop


def reset_character():
    """Method for resetting the characters"""
    global CHARACTER_MAIN, SKELETON_INSTANCE, BOSS_INSTANCE

    CHARACTER_MAIN = CharacterMain(HERO, STATS.level, STATS, TILES)
    BOSS_INSTANCE = Boss(STATS.level, CHARACTER_MAIN, TILES)
    SKELETON_INSTANCE = Skeleton(STATS.level, CHARACTER_MAIN, TILES)

    SKELETON_INSTANCE.create_enemies()
    BOSS_INSTANCE.create_enemies()


def draw_canvas():
    """Drawing the tiles"""
    canvas.delete("all")
    canvas.create_rectangle(0, 0, WIDTH, HEIGHT + 10, fill='green')
    MAP_TILES.draw_tiles(canvas)

    CHARACTER_MAIN.createEnemies(canvas)
    HERO.create_hero(canvas)
    GAME_LAYOUT.create_info(canvas, HEIGHT)
    canvas.create_text(50, HEIGHT + 70,  fill="red", font="Times 20 italic bold",
                       text=f'Level {STATS.level}')

    enemy_stat = CHARACTER_MAIN.allCharacters
    char_pos = HEIGHT + 20
    for char in enemy_stat:
        key = "KEY" if char["key"] is 1 else ""
        text = f'{char["character"]} : HP: {char["hp"]}  __  Pos: {char["position"]} {key}'
        canvas.create_text(550, char_pos,  fill="green", font="Times 20 italic bold",
                           text=text)
        char_pos += 20

    if STATS.level_complete is True:
        # CHARACTER_MAIN.allCharacters = []
        reset_character()
        # Skeleton(STATS.level, CHARACTER_MAIN).createEnemies(canvas)
        # Boss(STATS.level, CHARACTER_MAIN).createEnemies(canvas)
        STATS.level_complete = False
        new_tiles = MAP_TILES.shuffle_tiles()
        print(new_tiles, "new tiles")
        # MAP_TILES.tiles = new_tiles
        HERO.hero_position = [0, 0]
        HERO.max_hero_hp = HERO.max_hero_hp + randint(1, 6)
        HERO.hero_hp = HERO.max_hero_hp
        HERO.hero_dp = HERO.hero_dp + randint(1, 6)
        HERO.hero_sp = HERO.hero_sp + randint(1, 6)
        print('next level', STATS.level)

    # if HERO.hero_position is [-1, -1]:
    if STATS.hero_killed is True:
        Hero(STATS.level, TILES).create_hero(canvas)
        # HERO = 'a'
        # CHARACTER_MAIN.allCharacters = []
        reset_character()
        STATS.hero_killed = False

    if CHARACTER_MAIN.skeletonStrike != '':

        GAME_LAYOUT.create_info_enemy(
            canvas, HEIGHT, CHARACTER_MAIN.skeletonStrike)


def key_press(key):
    i = HERO.hero_position[0]
    j = HERO.hero_position[1]
    print(len(CHARACTER_MAIN.skeletons), 'ii', 'level :', STATS.level)
    if key != 'SPACE' and HERO.move_time is 2:
        CHARACTER_MAIN.moveSkeletons()
    if key is 'LEFT':
        HERO.move_hero(img="HERO-left", i=-1 if i > 0 else 0)
    if key is 'RIGHT':
        HERO.move_hero(img="HERO-right", i=1 if i < 9 else 0)
    if key is 'UP':
        HERO.move_hero(img="HERO-up", j=-1 if j > 0 else 0)
    if key is 'DOWN':
        HERO.move_hero(img="HERO-down", j=1 if j < 9 else 0)
    if key is 'SPACE':
        HERO.strike_enemy(CHARACTER_MAIN)


tk.bind('<Left>', lambda event: key_press('LEFT'))
tk.bind('<Right>', lambda event: key_press('RIGHT'))
tk.bind('<Up>', lambda event: key_press('UP'))
tk.bind('<Down>', lambda event: key_press('DOWN'))
tk.bind('<space>', lambda event: key_press('SPACE'))

# Don't write anything after this while loop, because that won't be executed
# The main game loop, at the moment it calls the draw_screen function continuously


while True:
    draw_canvas()
    # tk.update_idletasks()

    CHARACTER_MAIN.strikeHero()
    CHARACTER_MAIN.updateSkeletons()
    CHARACTER_MAIN.levelUp()
    tk.update()

    # tk.mainloop()
