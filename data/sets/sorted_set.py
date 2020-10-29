def observed():
  observations = []

  for count in range(5):
    print("please enter an observation")
    observation = input() 
    observations.append(observation)
  
  return observations
def remove_observations(observations):
  print("do you wish to remove any observations?")
  answer=input()
  remove=None
  if answer=="yes":
    return remove = True
    
  elif answer=="no":
    return remove = False
  else:
    print("please enter either \"yes\" OR \"no\"")

def remove():
  print("enter a string representing the observation (e.g. \"Skyscraper\") to be removed")
    remove_string=input()
    remove_string





print(observed())
remove_observations(input) 

