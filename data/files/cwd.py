#check current working directory by using the method getcwd of the module os which displays the file path of the current working directory
def cwd():
  import os
  path = os.getcwd()
  print(f"the Current Working Directory is {path}")
  print("the directory contains the following:")
  
  #display the content of this directory using the method listdir of the module os
  for file in os.listdir(path):  
    print(file)

def run():
 cwd()
run()