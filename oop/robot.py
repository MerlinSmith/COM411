from inhabitant import Inhabitant
class Robot(Inhabitant):
  #class Attribute
  laws = "protect, obey and survive"
  # A class method
  def the_laws():
    print(Robot.laws)

  # initialiser (special instance method)
  def __init__(self, name="Robot", age="0"):
    super().__init__(name, age)

    # An instance attribute
    
  
  def __repr__(self):
    return f"robot(name={self.name}, age={self.age} and energy {self.energy})"

  def __str__(self):
    return f"My name is {self.name} , I am {self.age} years old and energy {self.energy}."
#instance methods are taken from Inhabitant
  
robot = Robot()
Robot.the_laws()
print(repr(robot))
robot.move(10)
print(repr(robot))
robot.eat(5)
print(repr(robot))
robot.eat(20)
print(repr(robot))



