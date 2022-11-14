class Animal:
  def move(self):
    print("moving!")
  def eat(self):
    print("eating!")

class Dog(Animal):
  def bark(self):
    print("barking!")
  def find_food(self):
    self.move()
    self.eat()
  def bark_10(self):
    bark()
    self.bark()
    self.bark()
    self.bark()
    self.bark()
    self.bark()
    self.bark()
    self.bark()
    self.bark()
    self.bark()
    

my_dog = Dog()
my_dog.bark()
my_dog.bark_10()

