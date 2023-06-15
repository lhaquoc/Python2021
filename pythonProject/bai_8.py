class Things:
    def __init__(self):
        print("I am Things")

    def run(self):
        print("I am running!")


class Inanimate(Things):
    pass

class Table(Inanimate):
    def __init__(self, legs=4, length=1.5, width=2.5):
        self.legs = legs
        self.length = length
        self.width = width

    def about_me(self):
        print(self.legs)
        print(self.length)
        print(self.width)

class Animate(Things):
    pass

class Animals(Animate):
    def move(self):
        pass
    def eat_food(self):
        pass

class Mammals(Animals):
    pass


class Giraffes(Mammals):
    def __init__(self, spots, height, h_unit, weight, w_unit):
        self.giraffe_spots = spots
        self.height = Unit(height, h_unit)
        self.weight = Unit(weight, w_unit)

    def show(self):
        print(self.weight.show())
        print(self.height.show())

    def find_food(self):
        self.move()
        print("I've found food!")
        self.eat_food()


class Unit:
    def __init__(self, number=0, unit="cm"): # 10 + cm
        self.number = number
        self.unit = unit

    def show(self):
        print(f'{self.number} {self.unit}')

# animate = Animate()
# animate.run()

my_gir = Giraffes(4, 4, "m", 2000, "kg")
my_gir.show()

# my_tab = Table(width=10)
# my_tab.about_me()
#
# my_unit = Unit(10, "cm")
# my_unit.show()