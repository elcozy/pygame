import time
from tkinter import *
from hero import Hero
from skeleton import Skeleton, Skeletons, MonsterLevel
from boss import Boss
from maps import MapTiles
from random import randint
from game_layout import GameLayout


# statics

IMG_SIZE = 72
WIDTH = 10 * IMG_SIZE
HEIGHT = 10 * IMG_SIZE
FILEPATH = 'assets/img/'

root = Tk()
root.title('Wanderer Game')
canvas = Canvas(root, width=WIDTH, height=HEIGHT + 40, bg='white')
canvas.pack()

hero = Hero(FILEPATH)
skeleton = Skeleton()
skeletonMain = Skeletons()
skeletonLevel = MonsterLevel()
boss = Boss()
gamelayout = GameLayout(hero, FILEPATH, IMG_SIZE)
mapTiles = MapTiles(FILEPATH, IMG_SIZE)
skeletonLevel.checkSkeletons()
# This method is called continuously by the main game loop


def draw_tiles():
    canvas.delete("all")
    canvas.create_rectangle(0, 0, WIDTH, HEIGHT + 10, fill='green')
    mapTiles.drawTiles(canvas)
    skeletonMain.createEnemies(canvas)
    gamelayout.createInfo(
        canvas,  WIDTH, HEIGHT, 8, 2, 5, 9)
    hero.createHero(canvas, IMG_SIZE)


skeleton.checkPosition()
boss.checkPosition()
# Binding keyboard key events to functions


# def dontMove():

def keyPress(key):
    x = hero.hero_position[0]
    y = hero.hero_position[1]

    if key == 'LEFT':
        hero.move(x=-1 if x > 0 else 0, img="hero-left")
        print('hrt')
    if key == 'RIGHT':
        hero.move(x=1 if x < 9 else 0, img="hero-right")
    if key == 'UP':
        hero.move(y=-1 if y > 0 else 0, img="hero-up")
    if key == 'DOWN':
        hero.move(y=1 if y < 9 else 0, img="hero-down")


root.bind('<Left>', lambda event: keyPress('LEFT'))
root.bind('<Right>', lambda event: keyPress('RIGHT'))
root.bind('<Up>', lambda event: keyPress('UP'))
root.bind('<Down>', lambda event: keyPress('DOWN'))

# Don't write anything after this while loop, because that won't be executed
# The main game loop, at the moment it calls the draw_screen function continuously

while True:
    draw_tiles()
    # draw_screen()
    root.update_idletasks()
    # skeleton.moveSkeletons()
    root.update()

    # if x is moving and it hit wall, it should move y
