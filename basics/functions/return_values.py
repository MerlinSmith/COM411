def sum_weights (beep, bop):
  total_weight = beep + bop
  return total_weight

def calc_avg_weight (beep, bop):
  average_weight = (beep + bop)/2
  
  return average_weight



def run():
  print("what is the weight of beep?")
  beep = float(input())
  print("what is the weight of bop?")
  bop = float(input())

  print("what would you like to calculate (sum or avaerage)?")
  calculation = input()

  if(calculation == "sum"):
    answer= sum_weights (beep, bop)
    print("the sum of beep and bop's weight is {:.2f}".format(answer))
  elif(calculation == "average"):
    answer= calc_avg_weight (beep, bop)
    print("the average of beep and bop's weight is {:.2f}".format(answer))
  else:
    print("action not recognised")

run()
