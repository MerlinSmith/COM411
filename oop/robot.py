class Robot():
  #class Attribute
  laws = "protect, obey and survive"
  MAX_ENERGY = 100

  # A class method
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Robot"
    self.age = 0
    self.energy = 100
    self.increase_energy = 0

  # instance methods
  def grow(self):
    self.age +=1
  
  def eat(self, increase_energy):
    if self.increase_energy < self.MAX_ENERGY:
      self.energy = self.energy + self.increase_energy
  
  def distance(self, decrease_energy):
    if (self.MAX_ENERGY + self.increase_energy) > 0:
      self.energy = self.energy - self.increase_energy

  def display(self):
    print(f"I am {self.name}")
  
  def __repr__(self):
    return f"robot(name={self.name}, age={self.age})"

  def __str__(self):
    return f"My name is {self.name} and I am {self.age} years old."

if (__name__ == "__main__"):
  robot = Robot()
  robot.display()
  print(robot.__str__())