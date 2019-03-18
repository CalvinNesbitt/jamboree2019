from read_lagrangian import *
import matplotlib.pyplot as plt
from plot_one_trajectory import *

# test one trajectory
traj = d[10]

print(traj)

plot_one_trajectory(traj)

traj2 = d[20]
plot_one_trajectory(traj2)
plt.show()
