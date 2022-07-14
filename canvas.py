import tkinter
import math
from enemy import Enemy
from enemy import astar

import settings


def create_grid(event=None):
    # Creates all vertical lines at intevals of 100
    for i in range(0, settings.w, 20):
        settings.c.create_line([(i, 0), (i, settings.h)], tag='grid_line')
    # Creates all horizontal lines at intevals of 100
    for i in range(0, settings.h, 20):
        settings.c.create_line([(0, i), (settings.w, i)], tag='grid_line')



def fillSquare(x, y, color):
    settings.c.create_rectangle(x, y, x+20, y+20, fill=color, outline = 'black')


def left_click(event):
    x = event.x
    y = event.y
    base = 20
    x = 20 * math.floor(x/base)
    y = 20 * math.floor(y/base)
    settings.matrix[math.floor(y/base)][math.floor(x/base)] = 1
    fillSquare(x, y, "blue")


def right_click(event):
    x = event.x
    y = event.y
    base = 20
    x = 20 * math.floor(x/base)
    y = 20 * math.floor(y/base)
    settings.matrix[math.floor(y/base)][math.floor(x/base)] = 0
    fillSquare(x, y, "green")


create_grid()


def print_matrix(event):
    lines = []
    for row in settings.matrix:
        lines.append(' '.join(str(x) for x in row))
    print('\n'.join(lines))
    print(" ")

    maze = settings.matrix

    start = (0, 0)
    end = (20, 20)

    path = astar(maze, start, end)
    print(path)




settings.c.bind('<B1-Motion>', left_click)
settings.c.bind('<B3-Motion>', right_click)
settings.c.bind('<Button-2>', print_matrix)

enemy1 = Enemy(20, 20, "red")




# add to window and show
settings.c.pack()
settings.root.mainloop()
