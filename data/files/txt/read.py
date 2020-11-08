#check current working directory by using the method getcwd of the module os which displays the file path of the current working directory
def search(file_path):
  print("searching...")
  with open(file_path) as file:
    for line in file.readlines():
      print(f"{line.strip()}")
    print("done")
def run():
  search("data/files/txt/locations.txt")

run()


