def steps():
  likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
  return (likelihoods)

def run():
  all_steps = steps()
  good_steps = []
  bad_steps = []
  
  for step in all_steps:
    if step[1]>=50:
    #add to bad steps
      bad_steps.append(step)
    else:
    #add to good steps 
      good_steps.append(step)
  print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")

run()
