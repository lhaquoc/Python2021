import bai_2
import bai_3
import bai_4
import bai_5
import bai_6


def menu():
    while True:
        print("1. Draw squares")
        print("2. Draw rainbow benzene")
        print("3. Draw line")
        print("0. Close program")
        n = int(input("enter n:"))
        if n == 1:
            function1()
        if n == 2:
            function2()
        if n == 3:
            function3()
        if n == 0:
            print("thoát chương trình")
            break


t, wn = bai_4.create_turtle()


def function1():
    t.clear()
    bai_4.draw_squares(t)


def function2():
    t.clear()
    bai_4.draw_rainbow_benzene(t)


def function3():
    t.clear()
    bai_4.move_forward(t)
