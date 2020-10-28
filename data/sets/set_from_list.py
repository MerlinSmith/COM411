def observed():
  observations = []

  for count in range(7):
    print("please enter an observation")
    observation = input() 
    observations.append(observation)
  
  return observations

def run():
  print("Counting observations...")

  observations = observed()

  observations_set = set()

  for observation in observations:
    occurrences = observations.count(observation)
     
    observations_set.add( (observation, occurrences) )

  for observation in observations_set:
    print("{} observed {} times".format(observation[0], observation[1]))

run() 
