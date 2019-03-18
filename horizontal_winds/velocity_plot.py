import numpy as np
import csv
import matplotlib.pyplot as plt

files = []
with open('velocity_x.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    x_vel = np.empty([9,9])
    r = 0
    for row in readCSV:
        for i in range(0,8):
            for j in range(0,8):
                x_vel[i, j] = row[1+i*9+j]
        if (r % 1000 == 0 or r == 0 or r == 1 or r == 9999):
            plt.clf()
            plt.imshow(x_vel, interpolation='nearest')
            plt.colorbar()
            fname = 'plots/x_vel_%03d.png' % r
            print('Saving frame', fname)
            plt.savefig(fname)
            files.append(fname)
        r += 1

print()
