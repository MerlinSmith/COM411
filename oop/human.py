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
  
class Human():

  MAX_ENERGY = 100

  def __init__(self, name, age, energy):
    self.name = name
    self.age = age
    self.energy = energy
  
  def display(self):
    print(f"I am {self.name} and {self.age} years old")
  
if (__name__ == "__main__"):
  human = Human("Merlin", 24, 30)
  human.display()
  