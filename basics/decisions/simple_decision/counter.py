print("enter the first number")
first_num=int(input())
print("enter the second number")
second_num=int(input())
print("enter the third number")
third_num=int(input())

even_numbers=0
odd_numbers=0

if(first_num % 2 == 0):
  even_numbers += 1
else:
  odd_numbers +=1
if(second_num % 2 == 0):
  even_numbers +=1
else:
  odd_numbers +=1
if(third_num % 2 == 0):
  even_numbers +=1
else:
  odd_numbers +=1

#print results with correct grammar
if(even_numbers==1):
  print("there are {} even number and {} odd numbers".format(even_numbers, odd_numbers))
elif(odd_numbers==1):
  print("there are {} even numbers and {} odd number".format(even_numbers, odd_numbers))
else:
  print("there are {} even numbers and {} odd numbers".format(even_numbers, odd_numbers))