import matplotlib.pyplot as plt
import random as rnd
def data():
  paths = {}
  print("what type of line would you like? (:, -- or -)")
  line_type=input() 
  print("what colour would you like? (r, g or b)")
  line_colour=input() 
  print("what marker style would you like? (o, s or ^)")
  marker_style=input() 

  paths = {'line_type':line_type, 'line_colour' : line_colour, 'marker_style' : marker_style}
  #paths['line_type'] = line_type
  #paths['line_colour'] = line_colour
  #paths['marker_style'] = marker_style
  #would also work
  return paths

def generate():
  print("How many lines would you like to display?")
  lines=int(input())
  for line in range(lines):
    datas = data()
    x= [0, rnd.randrange(1, 10)]
    y= [0, rnd.randrange(1, 10)]
    plt.plot(x, y, f"{datas['line_colour']}{datas['line_type']}{datas['marker_style']}")

def run():
  generate() 
  plt.show()
run() 
