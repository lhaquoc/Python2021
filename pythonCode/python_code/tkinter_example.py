from tkinter import *
import turtle
tk = Tk()
t = turtle.Pen()

def ve_hinh_tron():
    t.reset()
    t.hideturtle()
    size = int(size_entry.get())
    color = color_entry.get()
    t.color(color)
    t.circle(size)
    
        
def ve_ngoi_sao():
    t.reset()
    t.hideturtle()
    color = color_entry.get()
    t.color(color)
    for x in range(5):
        t.forward(int(size_entry.get()))
        t.right(144)
        
def ve_hinh_vuong():
    t.reset()
    t.hideturtle()
    color = color_entry.get()
    t.color(color)
    for i in range(5):
        t.forward(int(size_entry.get()))
        t.right(90)

def canvas_ve_hinh_vuong():
    canvas.create_rectangle(10,10,150,250,fill=color_entry.get())

def thoat():
    turtle.bye()
    tk.destroy()
    
try:    
    Label(tk, text='Size', font=('calibre',10, 'bold')).pack()
    size_entry = Entry(tk, width=35)
    size_entry.pack()
    Label(tk, text='Color', font=('calibre',10, 'bold')).pack()
    color_entry = Entry(tk, width=35)
    color_entry.pack()
    btn1 = Button(tk, width=20, text='ve hinh tron', command=ve_hinh_tron).pack()
    btn2 = Button(tk, width=20, text='ve hinh vuong', command=ve_hinh_vuong).pack()
    btn3 = Button(tk, width=20, text='ve ngoi sao', command=ve_ngoi_sao).pack()
    btn4 = Button(tk, width=20, text='thoat chuong trinh', command=thoat).pack()
    btn5 = Button(tk, width=20, text='canvas vuong', command=canvas_ve_hinh_vuong).pack()
    canvas = Canvas(tk, width=400, height=350)
    canvas.pack()
    tk.mainloop()
except ValueError:
    print('Please enter a number')
    sys.exit(1)
