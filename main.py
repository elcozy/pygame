from tkinter import *
from Hero import Hero

IMG_SIZE = 72
WIDTH = 10 * IMG_SIZE
HEIGHT = 10 * IMG_SIZE

root = Tk()
root.title('Wanderer Game')
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

hero = Hero()

# This method is called continuously by the main game loop

filesList = []
layoutArray = []
layoutFile = open('layout_structure.txt', 'r')
layoutLine = layoutFile.readlines()
currentLine = 0

for line in layoutLine:
    # filesList.append(line)
    layoutArray.append(line)
    # print('f------', line, layoutArray)
    # for index, block in enumerate(layoutArray):
    # print('-----x', block, index)
    # # print(block[0])
    # for i, x in enumerate(block):
    #     print(block[index][i])
    #     print('----')
    # lineIndex = 0
    # for struct in line:

    #     if struct == 'o':
    #         filesList.append([lineIndex, currentLine, 'root.floor'])
    #     else:
    #         filesList.append([lineIndex, currentLine, 'root.wall'])
    #     lineIndex += 1
    # currentLine += 1


def draw_screen():
    canvas.delete("all")
    # for i in filesList:
    #     for j in i:
    #         canvas.create_image(i[0] * IMG_SIZE, i[1] * IMG_SIZE,
    #                             image=root.floor if i[2] == 'root.floor' else root.wall, anchor=NW)

    # canvas.create_image(3 * IMG_SIZE, 0, image=root.boss, anchor=NW)
    row = 0
    for index, block in enumerate(layoutArray):
        print('-----x', block, index)
        # print(block[0])

        for i in range(len(block) - 1):
            print('----', i, block[i])
            canvas.create_image(i * IMG_SIZE, row * IMG_SIZE,
                                image=root.floor if block[i] == 'o' else root.wall, anchor=NW)
        if index == len(layoutArray) - 1:
            break
        row += 1
    canvas.create_image(hero.x * IMG_SIZE, hero.y *
                        IMG_SIZE, image=getattr(root, hero.img), anchor=NW)
    #   canvas.create_image(2 * IMG_SIZE, 0, image=root.skeleton, anchor=NW)

    # Loading images. You can access these loaded images from the root object.
    # For example: root.floor or getattr(root, "floor")


def load_images():
    dir = "images/"
    root.floor = PhotoImage(file=dir + "floor.png")
    root.wall = PhotoImage(file=dir + "wall.png")
    root.hero_down = PhotoImage(file=dir + "hero-down.png")
    root.hero_up = PhotoImage(file=dir + "hero-up.png")
    root.hero_right = PhotoImage(file=dir + "hero-right.png")
    root.hero_left = PhotoImage(file=dir + "hero-left.png")
    root.skeleton = PhotoImage(file=dir + "skeleton.png")
    root.boss = PhotoImage(file=dir + "boss.png")


load_images()

# Binding keyboard key events to functions


def leftKey(event):
    hero.move(x=-1 if hero.x > 0 else 0, img="hero_left")


def rightKey(event):
    hero.move(x=1 if hero.x < 9 else 0, img="hero_right")


def upKey(event):
    hero.move(y=-1 if hero.y > 0 else 0, img="hero_up")


def downKey(event):
    hero.move(y=1 if hero.y < 9 else 0, img="hero_down")


root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<Up>', upKey)
root.bind('<Down>', downKey)

# Don't write anything after this while loop, because that won't be executed
# The main game loop, at the moment it calls the draw_screen function continuously
while True:
    draw_screen()
    root.update_idletasks()
    root.update()
