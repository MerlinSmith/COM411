print("please enter a word")
word = input()

def Display_Box(word):
  print("##" + "#"*len(word) + "##")
  print("# "+word+ " #") 
  print("##" + "#"*len(word) + "##")

def Display_Lower(word):
  print(word.lower())

def Display_Upper(word):
  print(word.upper())

def Display_Mirrored(word):
  reverse_word = ""
  for letter in reversed(word):
    reverse_word += letter
  print("{} | {}".format(word, reverse_word))

def Repeat():
  print("how many times would you like to display the word?")
  repeat_word = int(input ())
  print((word +"\n") * repeat_word)

def run():
  print("choose an option by typing the corresponding number:\n")
  print("1) Display in a Box – displays the word in an ascii art box")
  print("2) Display Lower-case – displays the word in lower-case e.g. hello\n")
  print("3) Display Upper-case – displays the word in upper-case e.g. HELLO\n")
  print("4) Display Mirrored – displays the word with its mirrored word e.g. Hello | olleH\n")
  print("5) Repeat – displays the word a chosen number of times, alternating between upper-case and lower-case.\n")

  answer = input()

  if answer == "1":
    Display_Box(word)
  elif answer == "2":
    Display_Lower(word)
  elif answer == "3":
    Display_Upper(word)
  elif answer == "4":
    Display_Mirrored(word)
  elif answer == "5":
    Repeat()
  else:
    print("incorrect input")

run()

