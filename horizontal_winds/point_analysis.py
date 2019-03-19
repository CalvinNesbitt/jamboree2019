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

def point_statistics_x(t0 = 7000, t1 = 9999, t2 = 19994, t3 = 19995, t4 = 19996):
    x_mean = np.zeros(82)
    x_ssq = np.zeros(82)
    with open('Data/velocity_x.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        j = -1
        for row in readCSV:
            if j >= t0:
                x_mean = x_mean + np.array(row).astype(float)
                x_ssq = x_ssq + np.square(np.array(row).astype(float))
            j += 1
        x_mean = (1/(t1-t0))*x_mean
        x_var = (x_ssq - (t1-t0)*np.square(x_mean))/(t1-t0)
        x_mean[0] = 0
        x_var[0] = 0
        plt.clf()
        plt.plot(x_mean, '.')
        fname = 'plots/x_mean_points.png'
        print('Saving frame', fname)
        plt.savefig(fname)
        plt.clf()
        plt.plot(x_var, '.')
        fname = 'plots/x_var_points.png'
        print('Saving frame', fname)
        plt.savefig(fname)

    with open('Data/predictions_x.csv', 'w') as csvfile:
        writeCSV = csv.writer(csvfile, delimiter=',')
        x_mean[0] = t2
        writeCSV.writerow(x_mean)
        x_mean[0] = t3
        writeCSV.writerow(x_mean)
        x_mean[0] = t4
        writeCSV.writerow(x_mean)
    with open('Data/variances_x.csv', 'w') as csvfile:
        writeCSV = csv.writer(csvfile, delimiter=',')
        x_var[0] = t2
        writeCSV.writerow(x_var)
        x_var[0] = t3
        writeCSV.writerow(x_var)
        x_var[0] = t4
        writeCSV.writerow(x_var)
    U = np.reshape(x_mean[1:82], (9,9))
    return U

def point_statistics_y(t0 = 7000, t1 = 9999, t2 = 19994, t3 = 19995, t4 = 19996):
    y_mean = np.zeros(82)
    y_ssq = np.zeros(82)
    with open('Data/velocity_y.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        j = -1
        for row in readCSV:
            if j >= t0:
                y_mean = y_mean + np.array(row).astype(float)
                y_ssq = y_ssq + np.square(np.array(row).astype(float))
            j += 1
    y_mean = (1/(t1-t0))*y_mean
    y_var = (y_ssq - (t1-t0)*np.square(y_mean))/(t1-t0)
    y_mean[0] = 0
    y_var[0] = 0
    plt.clf()
    plt.plot(y_mean, '.')
    fname = 'plots/y_mean_points.png'
    print('Saving frame', fname)
    plt.savefig(fname)
    plt.clf()
    plt.plot(y_var, '.')
    fname = 'plots/y_var_points.png'
    print('Saving frame', fname)
    plt.savefig(fname)

    with open('Data/predictions_y.csv', 'w') as csvfile:
        writeCSV = csv.writer(csvfile, delimiter=',')
        y_mean[0] = t2
        writeCSV.writerow(y_mean)
        y_mean[0] = t3
        writeCSV.writerow(y_mean)
        y_mean[0] = t4
        writeCSV.writerow(y_mean)
    with open('Data/variances_y.csv', 'w') as csvfile:
        writeCSV = csv.writer(csvfile, delimiter=',')
        y_var[0] = t2
        writeCSV.writerow(y_var)
        y_var[0] = t3
        writeCSV.writerow(y_var)
        y_var[0] = t4
        writeCSV.writerow(y_var)
    V = np.reshape(y_mean[1:82], (9,9))
    return V




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


quiver = 1 #set to 1 for quiver plot
if quiver == 1:
    n = 9
    X, Y = np.mgrid[0:n, 0:n]
    plt.clf()
    U = point_statistics_x().T
    V = point_statistics_y().T


    plt.quiver(X, Y, U, V, alpha=.5)
    plt.quiver(X, Y, U, V, edgecolor='k', facecolor='None', linewidth=.5)
    plt.xlim(0,8)
    fname = 'plots/big_mean.png'
    print('Saving frame', fname)
    plt.savefig(fname)
    plt.show()
