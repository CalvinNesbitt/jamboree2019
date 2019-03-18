import numpy
import csv

with open('velocity_x.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    x_vel = np.empty([9,9])
    colors = []
    #count = 0
    for row in readCSV:
        for i in range(0,8):
            for j in range(0,8):
                x_vel[i, j] = row[1+i*9+j]
            #count = count + 1
print(x_vel)
