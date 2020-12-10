class Inhabitant:

  MAX_ENERGY = 100

  def __init__(self, name = "Inhabitant", age = 0, energy=MAX_ENERGY):
    self.name = name
    self.age = age
    self.energy = Inhabitant.MAX_ENERGY
  
  def grow(self):
    self.age +=1
  
  def eat(self, food_amount):
    potential_energy = self.energy + food_amount
    if potential_energy > Inhabitant.MAX_ENERGY:
      self.energy = Inhabitant.MAX_ENERGY
      return potential_energy - self.energy
    else:
      self.energy = potential_energy
      return 0
    
  def move(self, distance_walked):
    if (self.energy - distance_walked) > 0:
      self.energy = self.energy - distance_walked

  def display(self):
    print(f"I am {self.name}")
  



  


