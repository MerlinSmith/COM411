import matplotlib.pyplot as plt

def read_data(file):
  temps=[]
  with open(file) as file:
    for line in file.readlines():
      print(f"{line.strip()}")
      temps.append(int(line.strip()))
  return temps


def run():
  data = read_data('visual/subplots/temps.txt')
  fig, axs = plt.subplots(1, 2, sharex='all') #determines number of subplots in the figure 

  fig.set_size_inches(8,4) #resizes the figure

  plt.xlabel("day")
  plt.ylabel("temperature") #labels x and y axis

  x = range(0, 7, 1)
  y = data

  axs[0].plot(x, y)
  axs[1].bar(x, y)
  
  plt.tight_layout()
  plt.show()

run()
