def display_ladder(steps):
  print("| |")
  
  for step in range(steps):
    print("***")
    print("| |")
  
def create_ladder():
  print("how many steps on the ladder?")
  steps=int(input())
  display_ladder(steps)
  
create_ladder()

