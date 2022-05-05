"""Laser module"""
import tkinter as tk  # Python 3.x
from game_constants import WIDTH, HEIGHT

import sys
import os

HALF_WIDTH = WIDTH / 2
HALF_HEIGHT = HEIGHT / 2

# master = tk.Tk()
# master.title('Game Over')


class Laser:
    """LAser class"""

    def __init__(self,  master):

        self.can = tk.Canvas(master, width=250,
                             height=150, bg='black')
        # self.rect = self.can.create_rectangle(
        #     205, 10, 300, 105, outline='black', fill='white')
        self.rect = self.can.create_text(
            125, 50, fill="red",
            font="Times 35 italic bold", text='GAME OVER')
        self.btn = tk.Button(master, text='Restart Game', width=10,
                             height=2, bd='2', command=self.restart_program)
        #  height=2, bd='2', command=master.destroy)

        self.btn.place(x=20, y=100)

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

    def restart_program(self):
        """Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        python = sys.executable
        os.execl(python, python, * sys.argv)


# # master = tk.Tk()
# # master.title('Game Over')
# L = Laser(master)
# master.mainloop()
