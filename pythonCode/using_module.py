import copy

class Animal:
    def __init__(self, species, number_of_legs, color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color

my_animal = Animal('dog', 4, 'brown')
my_animal_new = copy.copy(my_animal)
print(my_animal)
print(my_animal_new)
