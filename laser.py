"""Laser module"""

import sys
import os
import tkinter as tk
from game_constants import WIDTH, HEIGHT

HALF_WIDTH = WIDTH / 2
HALF_HEIGHT = HEIGHT / 2


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


class Laser:
    """LAser class"""

    def __init__(self,  master):

        self.can = tk.Canvas(master, width=250,
                             height=150, bg='black')
        self.rect = self.can.create_text(
            125, 50, fill="red",
            font="Times 35 italic bold", text='GAME OVER')
        self.btn = tk.Button(master, text='Restart Game', width=10,
                             height=2, bd='2', command=restart_program)
        self.btn2 = tk.Button(master, text='End Game', width=7,
                              height=2, bd='2', command=master.destroy)

        self.btn.place(x=10, y=100)
        self.btn2.place(x=150, y=100)

        self.can.focus()
        self.can.grid()
        self.color_ind = True
        self.flash()

    def flash(self):
        """Flashing the text"""
        color = "white"
        if self.color_ind:
            color = "red"
        self.can.itemconfigure(self.rect, fill=color)
        self.color_ind = not self.color_ind

        self.can.after(500, self.flash)
