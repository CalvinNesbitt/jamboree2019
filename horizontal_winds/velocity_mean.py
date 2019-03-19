import numpy as np
import csv
import matplotlib.pyplot as plt

n = 9
X, Y = np.mgrid[0:n, 0:n]

plot = 0


files = []
with open('velocity_x.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    x_vel = np.zeros([9,9])
    r = 0
    x_velt = np.zeros([9,9])
    for row in readCSV:
        for i in range(0,8):
            for j in range(0,8):
                x_velt[i, j] = row[1+i*9+j]
        x_vel = x_vel + x_velt
    x_avg = (1/9999)*x_vel
    plt.clf()
    plt.imshow(x_avg, interpolation='nearest')
    plt.colorbar()
    fname = 'plots/x_avg.png'
    print('Saving frame', fname)
    plt.savefig(fname)
    plt.clf()


with open('velocity_y.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    y_vel = np.zeros([9,9])
    r = 0
    y_velt = np.zeros([9,9])
    for row in readCSV:
        for i in range(0,8):
            for j in range(0,8):
                y_velt[i, j] = row[1+i*9+j]
        y_vel = y_vel + y_velt
    y_avg = (1/9999)*y_vel
    plt.clf()
    plt.imshow(y_avg, interpolation='nearest')
    plt.colorbar()
    fname = 'plots/y_avg.png'
    print('Saving frame', fname)
    plt.savefig(fname)
    files.append(fname)
    plt.clf()

U = x_avg[X, Y]
V = y_avg[X, Y]

plt.quiver(X, Y, U, V, alpha=.5)
plt.quiver(X, Y, U, V, edgecolor='k', facecolor='None', linewidth=.5)
plt.show()
