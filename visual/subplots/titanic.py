import csv 
import matplotlib.pyplot as plt
def read_data():
  with open("visual/subplots/titanic.csv") as csv_file :
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)

    first_key = header[0].strip()
    second_key = header[1].strip()
    data = {
      first_key:[],
      second_key:[]
     }
    for row in csv_reader:
      data[first_key].append(row[0].strip())
      data[second_key].append(row[1].strip())
    return data
    plt.show()

print(read_data())

    