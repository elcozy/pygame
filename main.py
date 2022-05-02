import time
from tkinter import *
from hero import Hero
from characters import Skeletons
from boss import Boss
from skel import Skel
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

hero = Hero()
skeletonMain = Skeletons(hero)

boss = Boss(skeletonMain)
boss.createEnemies(canvas)

skel = Skel(skeletonMain)
skel.createEnemies(canvas)

gamelayout = GameLayout(skeletonMain, hero, IMG_SIZE)
mapTiles = MapTiles(FILEPATH, IMG_SIZE)
stats = Stats()
# This method is called continuously by the main game loop
print(skeletonMain.skeletons)


def gameStatus():
    if hero.HERO_HP < 1:
        print('Game over')
        return 'Hero Killed'


def draw_tiles():
    canvas.delete("all")
    canvas.create_rectangle(0, 0, WIDTH, HEIGHT + 10, fill='green')
    mapTiles.drawTiles(canvas)

    # if gameStatus() == 'Hero Killed':
    #     stats.gameOver()
    # if gameStatus() != 'Hero Killed':
    skeletonMain.createEnemies(canvas)
    hero.createHero(canvas, IMG_SIZE)
    gamelayout.createInfo(canvas,  WIDTH, HEIGHT)

    enemyStat = skeletonMain.allCharacters
    charPos = HEIGHT + 20
    for char in enemyStat:
        canvas.create_text(500, charPos,  fill="green", font="Times 20 italic bold",
                           text=f'{char["character"]} : HP: {char["hp"]}/10 __  Pos: {char["position"]} ')
        charPos += 20

    if skeletonMain.skeletonStrike != '':
        gamelayout.createInfoEnemy(
            canvas,  WIDTH, HEIGHT, skeletonMain.skeletonStrike)
    # gameStatus()


def keyPress(key):
    x = hero.hero_position[0]
    y = hero.hero_position[1]
    print(skeletonMain.allCharacters, skeletonMain.skeletons, 'skeletons')

    if key != 'SPACE' and hero.moveTime == 2:
        skeletonMain.moveSkeletons()
    if key == 'LEFT':
        hero.moveHero(img="hero-left", x=-1 if x > 0 else 0)
    if key == 'RIGHT':
        hero.moveHero(img="hero-right", x=1 if x < 9 else 0)
    if key == 'UP':
        hero.moveHero(img="hero-up", y=-1 if y > 0 else 0)
    if key == 'DOWN':
        hero.moveHero(img="hero-down", y=1 if y < 9 else 0)
    if key == 'SPACE':
        hero.strikeEnemy(skeletonMain)


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

    skeletonMain.strikeHero()
    skeletonMain.updateSkeletons()
    # skeletonMain.moveSkeletons()
    root.update()

    # if x is moving and it hit wall, it should move y
