from tkinter import *
import random
import numpy as np



class MapTiles:

    def __init__(self, filePath, IMG_SIZE):
        self.level = 1
        self.IMG_SIZE = IMG_SIZE
        self.filePath = filePath
        self.tiles = []

        self.tileOpen = PhotoImage(
            file=f"{self.filePath}floor.png")

        self.tileBlock = PhotoImage(
            file=f"{self.filePath}wall.png")

    def drawTiles(self, canva):
        

        tileFile = open('tiles.txt', 'r').readlines()

        for line in tileFile:
            self.tiles.append(line)

        tileRow = 0
        
        
        
        for index, block in enumerate(self.tiles):
            for i in range(len(block) - 1):
                canva.create_image(i * self.IMG_SIZE, tileRow * self.IMG_SIZE,
                                   image=self.tileOpen if block[i] == 'o' else self.tileBlock, anchor=NW)
            if index == len(self.tiles) - 1:
                break
            tileRow += 1
