import turtle
import random
from tkinter import *

turtle.reset()

#turtle.color("yellow")
turtle.bgcolor("darkblue")
turtle.hideturtle()
turtle.speed(0)
color_lst=["red", "orange", "cyan", "yellow", "gray", "lightgreen"]
def starMaker(step, angle):
    for i in range(5):
        turtle.color(color_lst[random.randint(0,5)])
        turtle.forward(step)
        turtle.right(angle)
        
for i in range(10):
    turtle.penup()
    turtle.setpos(random.randint(-350, 350), random.randint(100, 300))
    turtle.pendown()
    starMaker(10, 144)

ts = turtle.getscreen()
ts.getcanvas().postscript(file="duck.eps")   
turtle.exitonclick()

