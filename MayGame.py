class Devices():
  pass
class Computer(Devices):

  pass
class MayGame(Devices):
  '''
  4 properties
  - model: string 
  - name: string
  - price: float
  - year: int
  '''
  # maygame = MayGame(model, name, price, year): initialization
  # define properties
  def __init__(self, model, name, price, year):
    self.model = model
    self.name = name
    self.price = price
    self.year = year
  '''
    5 methods - 5 actions
    - display
    - power_on
    - power_off
    - light_on
    - light_off
  '''
  # define methods (actions - functions) of this class
  def display(self):
    print(f'model: {self.model}\n')
    print(f'name: {self.name}\n')
    print(f'price: {self.price}\n')
    print(f'year: {self.year}\n')
    

  def power_on(self):
    print("powered on!")
    self.display()

  def power_off(self):
    print("powered off!")

  def light_on(self):
    print("lighted on!")

  def light_off(self):
    print("lighted off!")

class MayGameSamsung(MayGame):
  pass
'''
  use class MayGame
'''
maygamea = MayGame('Sony PS5', 'my gaming gear', 700, 2022)
my_comp = Computer()

print(f'{maygame.name}')
# power on
maygamea.power_on()
# light on
maygamea.light_on()
# power off
maygamea.power_off()
# light off
maygamea.light_off()