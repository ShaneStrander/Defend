
import tkinter

root = tkinter.Tk()

h = 800
w = 800

c = tkinter.Canvas(root, bg="green", height=h, width=w)

matrix = [[0 for x in range(w//20)] for y in range(h//20)]
