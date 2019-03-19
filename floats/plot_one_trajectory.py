import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
def plot_one_trajectory(traj):
    """ plots one trajectory which is a dictionary"""
    plt.plot(traj['lon'],traj['lat'])


def plot_one_trajectory_color(traj):
    """ plots one trajectory with colored dots
    SAD it doesn't work :((( """
    cmap = plt.cm.coolwarm(np.linspace(-10.,10.,50))
    fig, ax = plt.subplots()
    grid = np.array([np.array(traj['lon']),np.array(traj['lat'])]).T.reshape(-1,1,2)
    lc = LineCollection(grid, cmap="coolwarm")
    lc.set_array(np.array(traj['temp']))
    ax.add_collection(lc)
    ax.autoscale_view()
    plt.show()



def plot_temp_contour(d):
    """ plot temp contour plot"""
    for j in range(len(d)):
        lats = d[j]['lat']
        lon = np.mean(np.array(d[j]['lon']))
        temp = d[j]['temp']

        plt.plot(lats,temp)



def plot_temp_contour(d):
    """ plot temp contour plot"""
    meanlat = []
    meantemp = []
    meanlon = []
    for j in range(len(d)):
        lats = d[j]['lat']
        lon = np.mean(np.array(d[j]['lon']))
        temp = d[j]['temp']

        meanlat.append(np.mean(np.array(lats)))
        meantemp.append(np.mean(np.array(temp)))
        meanlon.append(lon)
    plt.contourf(np.array(meanlon),np.array(meanlat),np.array(meantemp))

