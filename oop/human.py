class Human():

  MAX_ENERGY = 100

  def __init__(self, name, age, energy, increase_energy):
    self.name = name
    self.age = age
    self.energy = energy
    self.increase_energy = 0
  
  #instance methods
  def grow(self):
    self.age +=1

  def display(self):
    print(f"I am {self.name} and {self.age} years old")
  
  def __repr__(self):
    return f"human (name={self.name}, age={self.age})"

  def __str__(self):
    return f"My name is {self.name} and I am {self.age} years old."
  
if (__name__ == "__main__"):
  human = Human("Merlin", 24, 30, 50)
  human.display()
  print(human.__repr__())

  