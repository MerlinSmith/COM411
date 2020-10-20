def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction by typing the corresponding index value:")
  dirs=directions() 

  for index in range(len(dirs)):
    print("index {}: {}".format(index, dirs[index]))

  user_in=int(input())
  return dirs[user_in]

def run():
  route = []
  print("working out escape route...")
  for count in range(5):
   direction = menu() 
   route.append(direction)
  print("escape route: {}".format(route))
 
run()








