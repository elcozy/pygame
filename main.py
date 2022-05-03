import time
from tkinter import *
from hero import Hero
from characters import CharacterMain
from boss import Boss
from skeleton import Skeleton
from maps import MapTiles
from random import randint
from gameStats import Stats
from game_layout import GameLayout

# statics

IMG_SIZE = 72 / 0.976
WIDTH = 10 * IMG_SIZE
HEIGHT = 10 * IMG_SIZE
FILEPATH = 'assets/img/'

root = Tk()
root.title('Wanderer Game')
canvas = Canvas(root, width=WIDTH, height=HEIGHT + 150, bg='white')
canvas.pack()


STATS = Stats()

HERO = Hero(STATS.level)

CHARACTER_MAIN = CharacterMain(HERO, STATS.level, STATS)

SKELETON_INSTANCE = Skeleton(STATS.level, CHARACTER_MAIN)
SKELETON_INSTANCE.create_enemies()

BOSS_INSTANCE = Boss(STATS.level, CHARACTER_MAIN)
BOSS_INSTANCE.create_enemies()


gamelayout = GameLayout(CHARACTER_MAIN, HERO, STATS)

MAP_TILES = MapTiles(FILEPATH, IMG_SIZE)
# This method is called continuously by the main game loop
print(CHARACTER_MAIN.skeletons)


def resetCharacter():
    global CHARACTER_MAIN, SKELETON_INSTANCE, BOSS_INSTANCE

    CHARACTER_MAIN = CharacterMain(HERO, STATS.level, STATS)
    SKELETON_INSTANCE = Skeleton(STATS.level, CHARACTER_MAIN)
    BOSS_INSTANCE = Boss(STATS.level, CHARACTER_MAIN)
    SKELETON_INSTANCE.createEnemies(canvas)
    BOSS_INSTANCE.createEnemies(canvas)


def gameStatus():
    if HERO.hero_hp < 1:
        print('Game over')
        return 'Hero Killed'


def draw_tiles():
    # print(level)
    canvas.delete("all")
    canvas.create_rectangle(0, 0, WIDTH, HEIGHT + 10, fill='green')
    MAP_TILES.drawTiles(canvas)

    # if gameStatus() == 'Hero Killed':
    #     STATS.gameOver()
    # if gameStatus() != 'Hero Killed':
    CHARACTER_MAIN.createEnemies(canvas)
    HERO.createHero(canvas, IMG_SIZE)
    gamelayout.create_info(canvas, HEIGHT)
    canvas.create_text(50, HEIGHT + 70,  fill="red", font="Times 20 italic bold",
                       text=f'Level {STATS.level}')

    enemy_stat = CHARACTER_MAIN.allCharacters
    charPos = HEIGHT + 20
    for char in enemy_stat:
        key = "KEY" if char["key"] == 1 else ""
        canvas.create_text(550, charPos,  fill="green", font="Times 20 italic bold",
                           text=f'{char["character"]} : HP: {char["hp"]}  __  Pos: {char["position"]} {key}')
        charPos += 20

    if STATS.level_complete == True:
        # CHARACTER_MAIN.allCharacters = []
        resetCharacter()
        # Skeleton(STATS.level, CHARACTER_MAIN).createEnemies(canvas)
        # Boss(STATS.level, CHARACTER_MAIN).createEnemies(canvas)
        STATS.level_complete = False
        HERO.hero_position = [0, 0]

        HERO.max_hero_hp = HERO.max_hero_hp + randint(1, 6)
        HERO.hero_hp = HERO.max_hero_hp
        HERO.hero_dp = HERO.hero_dp + randint(1, 6)
        HERO.hero_sp = HERO.hero_sp + randint(1, 6)
        print('next level', STATS.level)

    # if HERO.hero_position == [-1, -1]:
    if STATS.hero_killed == True:
        Hero(STATS.level).createHero(canvas, IMG_SIZE)
        # HERO = 'a'
        # CHARACTER_MAIN.allCharacters = []
        Skeleton(STATS.level, CHARACTER_MAIN).createEnemies(canvas)
        Boss(STATS.level, CHARACTER_MAIN).createEnemies(canvas)
        STATS.hero_killed = False

    if CHARACTER_MAIN.skeletonStrike != '':

        gamelayout.create_info_enemy(
            canvas, HEIGHT, CHARACTER_MAIN.skeletonStrike)
    # gameStatus()


def keyPress(key):
    x = HERO.hero_position[0]
    y = HERO.hero_position[1]
    print(len(CHARACTER_MAIN.skeletons), 'xx', 'level :', STATS.level)
    if key != 'SPACE' and HERO.moveTime == 2:
        CHARACTER_MAIN.moveSkeletons()
    if key == 'LEFT':
        HERO.moveHero(img="HERO-left", x=-1 if x > 0 else 0)
    if key == 'RIGHT':
        HERO.moveHero(img="HERO-right", x=1 if x < 9 else 0)
    if key == 'UP':
        HERO.moveHero(img="HERO-up", y=-1 if y > 0 else 0)
    if key == 'DOWN':
        HERO.moveHero(img="HERO-down", y=1 if y < 9 else 0)
    if key == 'SPACE':
        HERO.strikeEnemy(CHARACTER_MAIN)


root.bind('<Left>', lambda event: keyPress('LEFT'))
root.bind('<Right>', lambda event: keyPress('RIGHT'))
root.bind('<Up>', lambda event: keyPress('UP'))
root.bind('<Down>', lambda event: keyPress('DOWN'))
root.bind('<space>', lambda event: keyPress('SPACE'))

# Don't write anything after this while loop, because that won't be executed
# The main game loop, at the moment it calls the draw_screen function continuously


while True:
    print(HERO.hero_position)
    draw_tiles()
    root.update_idletasks()

    # time.sleep(1)

    CHARACTER_MAIN.strikeHero()
    CHARACTER_MAIN.updateSkeletons()
    CHARACTER_MAIN.levelUp()
    # CHARACTER_MAIN.moveSkeletons()
    root.update()

    # if x is moving and it hit wall, it should move y
