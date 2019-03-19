import numpy as np
import csv
import matplotlib.pyplot as plt
# from _future__ import division

def point_analysis(t0 = 7000, t1 = 9999):
    with open('Data/velocity_x.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        x_vel = np.zeros(t1 - t0)
        j = -1
        for row in readCSV:
            if j >= t0:
                x_vel[j-t0] = row[i]
            j += 1

            plt.clf()
            plt.plot(x_vel)
            fname = 'plots/x_vel_point_%03d.png' % i
            print('Saving frame', fname)
            plt.savefig(fname)

def point_statistics_x(t0 = 7000, t1 = 9999):
    with open('Data/velocity_x.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        x_mean = np.zeros(82)
        j = -1
        for row in readCSV:
            if j >= t0:
                x_mean = x_mean + np.array(row).astype(float)
            j += 1
        x_mean = (1/(t1-t0))*x_mean
        x_mean[0] = 0
        plt.clf()
        plt.plot(x_mean, '.')
        fname = 'plots/x_mean_points.png'
        print('Saving frame', fname)
        plt.savefig(fname)

def point_statistics_y(t0 = 7000, t1 = 9999):
    with open('Data/velocity_y.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        y_mean = np.zeros(82)
        j = -1
        for row in readCSV:
            if j >= t0:
                y_mean = y_mean + np.array(row).astype(float)
            j += 1
        y_mean = (1/(t1-t0))*y_mean
        y_mean[0] = 0
        plt.clf()
        plt.plot(y_mean, '.')
        fname = 'plots/y_mean_points.png'
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


point_statistics_y()
