import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=800)
canvas.pack()
canvas.create_polygon(410, 410, 410, 460, 450, 435)
for x in range(0, 100):
    canvas.move(1, -5, 0)
    tk.update()
    time.sleep(0.05)
