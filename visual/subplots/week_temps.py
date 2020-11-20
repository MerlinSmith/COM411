import csv
import matplotlib.pyplot as plt
first_key = None
second_key = None
def read_data():
  global first_key, second_key
  with open("visual/subplots/temps.csv") as csvfile:
      csv_reader = csv.reader(csvfile)
      header = next(csv_reader) #fetches next row
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

def run():
  data = read_data()
  
  fig, (ax1, ax2) = plt.subplots(2, 1, sharex = 'all')
  ax1.plot(range(1,8), data[first_key])
  ax2.plot(range(1,8), data[second_key])
  plt.tight_layout()
  plt.show()
run()

    
 

    
    