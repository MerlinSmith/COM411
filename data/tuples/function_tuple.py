def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return min(likelihoods), max(likelihoods)

def run():
  likely = likelihood() 
  print(f"Minimum likelihood of falling: {likely[0]}%")
  print(f"Maximum likelihood of falling: {likely[1]}%")

run() 

