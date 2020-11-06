def observed():
  observations = []

  for count in range(5):
    print("please enter an observation")
    observation = input() 
    observations.append(observation)
  
  return observations

def remove_observations(obs):
  is_running=True
  while (is_running):

    print("do you wish to remove any observations? type \"yes\" or \"no\" ")
    answer = str(input())

    if answer=="yes":
      print("what would you like to to remove?")
      remove_string = str(input())
      repetitions = obs.count(remove_string)
      i=0
      while i < repetitions:
        obs.remove(remove_string) 
        print(remove_string + " removed")
        i +=1
    
    elif answer=="no":
      print("nothing removed")
      is_running=False
    else:
      print("please enter either \"yes\" OR \"no\"")
    return obs
def run():
  obs = observed()
  
  observations = remove_observations(obs)
  observations_set = set()

  for observation in observations:
    occurrences = observations.count(observation)
     
    observations_set.add( (observation, occurrences) )

  for observation in observations_set:
    print("{} observed {} times".format(observation[0], observation[1]))

run()










