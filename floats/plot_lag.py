from read_lagrangian import *
import matplotlib.pyplot as plt
from plot_one_trajectory import *


plot_temp_contour(d)
plt.show()
exit()
for j in range(0,10):
   # get jth trajectory 
   traj = d[j]


   plot_one_trajectory_color(traj)
