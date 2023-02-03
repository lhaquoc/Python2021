from tkinter import *
from tkinter import colorchooser
import random

def random_rectangle(width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, y2, y2, fill=fill_color)

def choose_color():
    color_code = colorchooser.askcolor(title ="Choose color")
    print(color_code)
    random_rectangle(200, 200, color_code[1])
    
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

button = Button(tk, text="Select color", command=choose_color)
button.pack()
