# PLOTS FOR THE PRESENTATION IN HERE

import json
import numpy as np
import matplotlib.pyplot as plt
# =============================================================================
# Random seed
# =============================================================================
np.random.seed(seed = 0)
val_idx = []
for i in range(100):
      r=np.random.randint(0,600)
      if r not in val_idx: val_idx.append(r)
val_idx = np.array(val_idx)
a = np.arange(600)
trn_idx = a[np.invert(np.isin(a,val_idx))]

with open('lagrangian.json') as infile:
    d = json.load(infile)

d_trn = list(d[i] for i in val_idx)
d_val = list(d[i] for i in trn_idx)




from velocity import get_velocity
Ntrn = len(d_trn)
characteristics = ['mean u','mean v','var u','var v','variance x','variance y','mean temp','mean var',
                           'direction x', 'direction y','standing eddy kinetic energy','kinetic energy','gyration']
# add more tomorrow
#temp gradient in x and y, speed, overall direction of trajectory,
trajectory_signature = np.zeros((600,len(characteristics)))
y = np.zeros((600,2))
for j in range(600):
    vel=get_velocity(d[j]['lat'],d[j]['lon'],d[j]['dt'])
    # outputs: mean longitude and latitude
    y[j,0]=np.mean(np.array(d[j]['lon']))
    y[j,1]=np.mean(np.array(d[j]['lat']))

    # characteristics of the trajectory
    # mean u and v
    trajectory_signature[j,0]=np.mean(vel[0])
    trajectory_signature[j,1]=np.mean(vel[1])
    # variance u and v
    trajectory_signature[j,2]=np.var(vel[0])
    trajectory_signature[j,3]=np.var(vel[1])
    # variance in x and y - how close trajectory stays to its centre
    trajectory_signature[j,4]=np.var(np.array(d[j]['lon']))
    trajectory_signature[j,5]=np.var(np.array(d[j]['lat']))
    # mean and var temp
    trajectory_signature[j,6] = np.mean(np.array(d[j]['temp']))
    trajectory_signature[j,7] = np.var(np.array(d[j]['temp']))
    # direction of trajectory
    end_point = len(d[j]['lon'])-1
    start_point = 0
    trajectory_signature[j,8] = d[j]['lon'][end_point] - d[j]['lon'][start_point]
    end_point = len(d[j]['lat'])-1
    start_point = 0
    trajectory_signature[j,9] = d[j]['lat'][end_point] - d[j]['lat'][start_point]
    # kinetic energy stuff
    u = np.array(vel[0])
    v = np.array(vel[1])
    umean = np.mean(u)
    vmean = np.mean(v)
    seke = np.sqrt( np.mean((u-umean)**2)+np.mean((v-vmean)**2) )
    ke = (np.mean(u)**2+np.mean(v)**2)
    trajectory_signature[j,10] = seke
    trajectory_signature[j,11] = ke

    # radius of gyration
    x = np.array(d[j]['lon'])
    y = np.array(d[j]['lat'])
    xmean = np.mean(x)
    ymean = np.mean(y)
    r2 = (x-xmean)**2 + (y-ymean)**2
    rg = np.sqrt(np.sum(r2))/(len(r2))
    trajectory_signature[j,12] = rg







for i in range(len(characteristics)):
    plt.clf()
    xfull = trajectory_signature[:,i]
    x = xfull[~np.isnan(xfull)]
    meanlon = y[:,0]
    meanlon = meanlon[~np.isnan(xfull)]
    plt.plot(x,meanlon,'x')
     
    plt.xlabel(characteristics[i])
    plt.ylabel('mean lon')
    plt.savefig('plots/mean_lon_vs_'+characteristics[i]+'.png')
    plt.clf()
    meanlat = y[:,1]
    meanlat = meanlat[~np.isnan(xfull)]
    plt.plot(x,meanlat,'x')

    plt.xlabel(characteristics[i])
    plt.ylabel('mean lat')
    plt.savefig('plots/mean_lat_vs_'+characteristics[i]+'.png')

