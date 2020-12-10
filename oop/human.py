from inhabitant import Inhabitant
class Human(Inhabitant):

  MAX_ENERGY = 100
  #magic methods
  def __init__(self, name="Human", age="0"):
    super().__init__(name, age)
  
  def __repr__(self):
    return f"human (name={self.name}, age={self.age} and energy={self.energy})"

  def __str__(self):
    return f"My name is {self.name} , I am {self.age} years old and energy {self.energy}."
  
  #instance methods

  
if (__name__ == "__main__"):
  human = Human()
  print(repr(human))
  human.move(10)
  print(repr(human))
  human.eat(5)
  print(repr(human))
  human.eat(20)
  