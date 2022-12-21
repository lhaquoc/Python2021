import random

from tkinter import*
tk = Tk()

def exit():
    tk.destroy()

def hinh_vuong_canvas():
    canvas.delete('all')
    #canvas.create_rectangle(int(color_entry.get()))
    #canvas.create_rectangle(10,10,150,150,fill=color_entry.get())
    #print(ve_hinh_vuong_canvas_entry.get())
    #print(ve_hinh_vuong_canvas_entry.get().split(','))
    input_hinh_vuong=ve_hinh_vuong_canvas_entry.get().split(',')
    x1=int(input_hinh_vuong[0])
    y1=int(input_hinh_vuong[1])
    x2=int(input_hinh_vuong[2])
    y2=int(input_hinh_vuong[3])
    color_hinh_vuong=input_hinh_vuong[4]
    canvas.create_rectangle(x1,y1,x2,y2,fill=color_hinh_vuong)

def polygons_canvas():
    canvas.delete('all')
    canvas.create_polygon(10, 10, 100, 10, 100, 110, fill=color_entry.get())

Label(tk, text='Size',font=("Helvetica",10)).pack()
size_entry = Entry(tk,width=40)
size_entry.pack()

Label(tk, text='color',font=("Helvetica",10)).pack()
color_entry= Entry(tk, width=40)
color_entry.pack()

Label(tk, text='ve hinh vuong canvas',font=("Helvetica",10)).pack()
ve_hinh_vuong_canvas_entry=Entry(tk,width=40)
ve_hinh_vuong_canvas_entry.pack()

btn= Button(tk, width=20,text='Star',command=star_maker)
btn.pack()

btn1= Button(tk,width=20,text='circle',command=hinh_tron)
btn1.pack()

btn2= Button(tk,width=20,text='squade',command=hinh_vuong)
btn2.pack()

btn3= Button(tk,width=20,text='exit',command=exit1)
btn3.pack()

canvas1= Button(tk,width=20,text='ve hinh vuong canvas',command=hinh_vuong_canvas)
canvas1.pack()

canvas2= Button(tk,width=20,text='polygons canvas',command=polygons_canvas)
canvas2.pack()

canvas = Canvas(tk,width=500,height=500)
canvas.pack()

#canvas.create_line(0,0,500,500)
#canvas.create_rectangle(10,10,100,100)


def random_rectangle(width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = random.randrange(x1 + random.randrange(width))
    y2 = random.randrange(y1 + random.randrange(height))
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)

#for i in range(20):
    #random_rectangle(500,500,red)
canvas.create_text(300, 300, text='Opportunities don\'t happen, you create them')
