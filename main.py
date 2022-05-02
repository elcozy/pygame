import time
from tkinter import *
from hero import Hero
from characters import CharacterMain
from boss import Boss
from skeleton import Skeleton
from maps import MapTiles
from random import randint
from game_layout import GameLayout
from gameStats import Stats

# statics

IMG_SIZE = 72 / 0.976
WIDTH = 10 * IMG_SIZE
HEIGHT = 10 * IMG_SIZE
FILEPATH = 'assets/img/'

root = Tk()
root.title('Wanderer Game')
canvas = Canvas(root, width=WIDTH, height=HEIGHT + 150, bg='white')
canvas.pack()


stats = Stats()

hero = Hero(stats.level)

characterMain = CharacterMain(hero, stats.level, stats)

skel = Skeleton(stats.level, characterMain)
skel.createEnemies(canvas)

boss = Boss(stats.level, characterMain)
boss.createEnemies(canvas)


gamelayout = GameLayout(characterMain, hero, IMG_SIZE, stats)

mapTiles = MapTiles(FILEPATH, IMG_SIZE)
# This method is called continuously by the main game loop
print(characterMain.skeletons)


def gameStatus():
    if hero.HERO_HP < 1:
        print('Game over')
        return 'Hero Killed'


def draw_tiles():
    # print(level)
    canvas.delete("all")
    canvas.create_rectangle(0, 0, WIDTH, HEIGHT + 10, fill='green')
    mapTiles.drawTiles(canvas)

    # if gameStatus() == 'Hero Killed':
    #     stats.gameOver()
    # if gameStatus() != 'Hero Killed':
    characterMain.createEnemies(canvas)
    hero.createHero(canvas, IMG_SIZE)
    gamelayout.createInfo(canvas,  WIDTH, HEIGHT)
    canvas.create_text(50, HEIGHT + 70,  fill="red", font="Times 20 italic bold",
                       text=f'Level {stats.level}')

    enemyStat = characterMain.allCharacters
    charPos = HEIGHT + 20
    for char in enemyStat:
        key = "KEY" if char["key"] == 1 else ""
        canvas.create_text(550, charPos,  fill="green", font="Times 20 italic bold",
                           text=f'{char["character"]} : HP: {char["hp"]}  __  Pos: {char["position"]} {key}')
        charPos += 20

    if stats.levelComplete == True:
        characterMain.allCharacters = []
        Skeleton(stats.level, characterMain).createEnemies(canvas)
        Boss(stats.level, characterMain).createEnemies(canvas)
        stats.levelComplete = False
        print('next level', stats.level)

    # if hero.hero_position == [-1, -1]:
    if stats.heroKilled == True:
        Hero(stats.level).createHero(canvas, IMG_SIZE)
        # hero = 'a'
        characterMain.allCharacters = []
        Skeleton(stats.level, characterMain).createEnemies(canvas)
        Boss(stats.level, characterMain).createEnemies(canvas)
        stats.heroKilled = False

    if characterMain.skeletonStrike != '':

        gamelayout.createInfoEnemy(
            canvas,  WIDTH, HEIGHT, characterMain.skeletonStrike)
    # gameStatus()


def keyPress(key):
    x = hero.hero_position[0]
    y = hero.hero_position[1]
    print(len(characterMain.skeletons), 'xx', 'level :', stats.level)
    if key != 'SPACE' and hero.moveTime == 2:
        characterMain.moveSkeletons()
    if key == 'LEFT':
        hero.moveHero(img="hero-left", x=-1 if x > 0 else 0)
    if key == 'RIGHT':
        hero.moveHero(img="hero-right", x=1 if x < 9 else 0)
    if key == 'UP':
        hero.moveHero(img="hero-up", y=-1 if y > 0 else 0)
    if key == 'DOWN':
        hero.moveHero(img="hero-down", y=1 if y < 9 else 0)
    if key == 'SPACE':
        hero.strikeEnemy(characterMain)


root.bind('<Left>', lambda event: keyPress('LEFT'))
root.bind('<Right>', lambda event: keyPress('RIGHT'))
root.bind('<Up>', lambda event: keyPress('UP'))
root.bind('<Down>', lambda event: keyPress('DOWN'))
root.bind('<space>', lambda event: keyPress('SPACE'))

# Don't write anything after this while loop, because that won't be executed
# The main game loop, at the moment it calls the draw_screen function continuously


while True:
    draw_tiles()
    root.update_idletasks()

    # time.sleep(1)

    characterMain.strikeHero()
    characterMain.updateSkeletons()
    characterMain.levelUp()
    # characterMain.moveSkeletons()
    root.update()

    # if x is moving and it hit wall, it should move y
