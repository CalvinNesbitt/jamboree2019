import numpy as np
import csv
import matplotlib.pyplot as plt
# from _future__ import division

def point_analysis(i):
    with open('Data/velocity_x.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        x_vel = np.zeros(2999)
        j = -1
        for row in readCSV:
            if j >= 7000:
                x_vel[j-7000] = row[i]
            j += 1

    plt.clf()
    plt.plot(x_vel)
    fname = 'plots/x_vel_point_%03d.png' % i
    print('Saving frame', fname)
    plt.savefig(fname)

def mean_point_x():
    with open('Data/velocity_x.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        x_vel = np.zeros(2999)
        j = -1
        for row in readCSV:
            if j >= 7000:
                x_vel[j-7000] = (np.sum(np.array(row).astype(float))-float(row[0]))/81
            j += 1

    plt.clf()
    plt.plot(x_vel)
    fname = 'plots/x_vel_point_mean.png'
    print('Saving frame', fname)
    plt.savefig(fname)

def mean_point_y():
    with open('Data/velocity_y.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        y_vel = np.zeros(2999)
        j = -1
        for row in readCSV:
            if j >= 7000:
                y_vel[j-7000] = (np.sum(np.array(row).astype(float))-float(row[0]))/81
            j += 1

    plt.clf()
    plt.plot(y_vel)
    fname = 'plots/y_vel_point_mean.png'
    print('Saving frame', fname)
    plt.savefig(fname)


for i in range(20, 40):
    point_analysis(i)
