from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=800)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)


def moveObject(event):
    canvas.move(1, 5, 0)


canvas.bind_all('<KeyPress-Return>', moveObject)
tk.mainloop()
