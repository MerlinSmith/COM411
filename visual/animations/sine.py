import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()
    
def animate(frame):
  global ax    
  ax.set_xlim(0, 720)
  ax.set_ylim(-1, 1)
  x = np.arange(0, frame)
  x_radians = (x * (np.pi/180))
  y = np.sin(x_radians)
  ax.plot(x, y, 'r') 
def run():
  global fig  
  simple_animation = animation.FuncAnimation(fig, animate, frames = 720, interval = 100)
  plt.show()
  
      
run()  

