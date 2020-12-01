class Robot():
  #class Attribute
  laws = "protect, obey and survive"

  # A class method
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Robot"
    self.age = 0

  # An instance method
  def display(self):
    print(f"I am {self.name}")
  
  def __repr__(self):
    return f"robot(name={self.name}, age={self.age})"

  def __str__(self):
    return f"My name is {self.name} and I am {self.age} years old."
  
class Human():

  MAX_ENERGY = 100

  def __init__(self, name, age, energy):
    self.name = name
    self.age = age
    self.energy = energy
  
  def display(self):
    print(f"I am {self.name} and {self.age} years old")
  
  def __repr__(self):
    return f"human (name={self.name}, age={self.age})"

  def __str__(self):
    return f"My name is {self.name} and I am {self.age} years old."
  
if (__name__ == "__main__"):
  human = Human("Merlin", 24, 30)
  human.display()
  print(human.__repr__())

if (__name__ == "__main__"):
  robot = Robot()
  robot.display()
  print(robot.__str__())

  