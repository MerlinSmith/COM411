print("program started")
print("Please enter an ASCII code:")
num=int(input())

asc_val = chr(num)

lowVal=32
highVal=127

if num in range(lowVal, highVal):
  print("the character represented by ASCII code {} is {}".format(num, asc_val))
else:
  print("input not within range 32-126")
print("program ended")