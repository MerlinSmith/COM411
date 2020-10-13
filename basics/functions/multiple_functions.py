def display_ladder(steps):
  
  print("| |")
  print("***")
  

  
 

def create_ladder():
  print("how many steps on the ladder?")
  num=input()
  count=0
  while(count<int(num)):
    display_ladder(num)
    count=count+1
  else:
    print("| |")
create_ladder()

