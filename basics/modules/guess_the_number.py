def play_guess_the_number():
  print("Please enter the minimum value:") 
  min = int(input())
  print("Please enter the maximum value:")
  max = int(input())
  print("I am thinking of a number between {} and {}.  Can you guess what it is?".format(min, max))
  import random
  random_number = random.randrange(min, max)
  guess = 0

  while (guess != random_number):
    guess=int(input())

    if(guess == random_number):
      print("congrats!")
      break
    elif(guess < random_number):
      print("guess higher")
    elif(guess > random_number):
      print("guess lower")

  print("Game Over")
  
play_guess_the_number()