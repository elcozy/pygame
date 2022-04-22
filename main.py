import time
from tkinter import *
from Hero import Hero
from Skeleton import Skeleton
from Boss import Boss
from Layout import *
IMG_SIZE = 72
WIDTH = 10 * IMG_SIZE
HEIGHT = 10 * IMG_SIZE

root = Tk()
root.title('Wanderer Game')
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

hero = Hero()
skeleton = Skeleton()
boss = Boss()

# This method is called continuously by the main game loop


def draw_screen():
    canvas.delete("all")
    row = 0
    for index, block in enumerate(layoutArray):
        # print('-----x', block, index)
        for i in range(len(block) - 1):
            # print('----', i, block[i])
            canvas.create_image(i * IMG_SIZE, row * IMG_SIZE,
                                image=root.floor if block[i] == 'o' else root.wall, anchor=NW)
        if index == len(layoutArray) - 1:
            break
        row += 1
    canvas.create_image(boss.x * IMG_SIZE, boss.y *
                        IMG_SIZE, image=root.boss, anchor=NW)

    canvas.create_image(hero.x * IMG_SIZE, hero.y *
                        IMG_SIZE, image=getattr(root, hero.img), anchor=NW)
    canvas.create_image(skeleton.x * IMG_SIZE,
                        skeleton.y * IMG_SIZE, image=root.skeleton, anchor=NW)

    # Loading images. You can access these loaded images from the root object.
    # For example: root.floor or getattr(root, "floor")


def load_images():
    dir = "assets/img/"

    root.floor = PhotoImage(file=dir + "floor.png")
    root.wall = PhotoImage(file=dir + "wall.png")
    root.hero_down = PhotoImage(file=dir + "hero-down.png")
    root.hero_up = PhotoImage(file=dir + "hero-up.png")
    root.hero_right = PhotoImage(file=dir + "hero-right.png")
    root.hero_left = PhotoImage(file=dir + "hero-left.png")
    root.skeleton = PhotoImage(file=dir + "skeleton.png")
    root.boss = PhotoImage(file=dir + "boss.png")


load_images()
skeleton.start()
# Binding keyboard key events to functions


# def dontMove():

def keyPress(key):
    if key == 'LEFT':
        hero.move(x=-1 if hero.x > 0 else 0, img="hero_left")
    if key == 'RIGHT':
        hero.move(x=1 if hero.x < 9 else 0, img="hero_right")
    if key == 'UP':
        hero.move(y=-1 if hero.y > 0 else 0, img="hero_up")
    if key == 'DOWN':
        hero.move(y=1 if hero.y < 9 else 0, img="hero_down")


root.bind('<Left>', lambda event: keyPress('LEFT'))
root.bind('<Right>', lambda event: keyPress('RIGHT'))
root.bind('<Up>', lambda event: keyPress('UP'))
root.bind('<Down>', lambda event: keyPress('DOWN'))

# Don't write anything after this while loop, because that won't be executed
# The main game loop, at the moment it calls the draw_screen function continuously
while True:
    draw_screen()
    root.update_idletasks()
    root.update()
