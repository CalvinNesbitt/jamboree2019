import json
import numpy as np
import matplotlib.pyplot as plt
# =============================================================================
# Random seed: separate train and validation
# =============================================================================
np.random.seed(seed = 1)
val_idx = []
boole=True
Ntest = 1
while boole:
      r=np.random.randint(0,600)
      if r not in val_idx: val_idx.append(r)
      val = np.size(val_idx)
      if val == Ntest:
           boole=False
val_idx = np.array(val_idx)
a = np.arange(600)
trn_idx = a[np.invert(np.isin(a,val_idx))]

# =============================================================================
# Open file
# =============================================================================

with open('lagrangian.json') as infile:
    d = json.load(infile)

# =============================================================================
# Get characteristics of trajectories for inputs X
# and mean of lon and lat for outputs y
# =============================================================================

from velocity import *

characteristics = ['mean u','mean v','var u','var v','variance x','variance y','mean temp','var temp',
                           'direction x', 'direction y','gyration','kinetic energy','standing eddy kinetic energy',
                           'temp gradient with time','temp gradient with time/umean','temp gradientwith time/vmean',
                           'mean |u|','mean|v|','var |u|','var|v|']
# add more tomorrow
#temp gradient in x and y, speed, overall direction of trajectory,
trajectory_signature = np.zeros((600,len(characteristics)))
y = np.zeros((600,2))
for j in range(600):
    vel=get_velocity(d[j]['lat'],d[j]['lon'],d[j]['dt'])
    # outputs: mean longitude and latitude
    y[j,0]=np.nanmean(np.array(d[j]['lon']))
    y[j,1]=np.nanmean(np.array(d[j]['lat']))

    # characteristics of the trajectory
    # mean u and v
    trajectory_signature[j,0]= np.nanmean(vel[0])
    trajectory_signature[j,1]= np.nanmean(vel[1])
    # variance u and v
    trajectory_signature[j,2]= np.nanvar(vel[0])
    trajectory_signature[j,3]= np.nanvar(vel[1])
    # variance in x and y - how close trajectory stays to its centre
    trajectory_signature[j,4]= np.nanvar(np.array(d[j]['lon']))
    trajectory_signature[j,5]= np.nanvar(np.array(d[j]['lat']))
    # mean and var temp
    for i in range(len(d[j]['temp'])):
        if d[j]['temp'][i] == np.inf:
            d[j]['temp'][i] = np.nan

    trajectory_signature[j,6] = np.nanmean(np.array(d[j]['temp']))
    trajectory_signature[j,7] = np.nanvar(np.array(d[j]['temp']))
    # direction of trajectory
    end_point = len(d[j]['lon'])-1
    start_point = 0
    trajectory_signature[j,8] = d[j]['lon'][end_point] - d[j]['lon'][start_point]
    end_point = len(d[j]['lat'])-1
    start_point = 0
    trajectory_signature[j,9] = d[j]['lat'][end_point] - d[j]['lat'][start_point]
    # radius of gyration
    xl = np.array(d[j]['lon'])
    yl = np.array(d[j]['lat'])
    xmean = np.nanmean(xl)
    ymean = np.nanmean(yl)
    r2 = (xl-xmean)**2 + (yl-ymean)**2
    rg = np.sqrt(np.sum(r2)/len(r2))
    trajectory_signature[j,10] = rg
    # kinetic energy stuff
    u = np.array(vel[0])
    v = np.array(vel[1])
    umean = np.nanmean(u)
    vmean = np.nanmean(v)
    seke = np.sqrt( np.nanmean((u-umean)**2)+np.nanmean((v-vmean)**2) )
    ke = (np.nanmean(u)**2+np.nanmean(v)**2)
    trajectory_signature[j,11] = ke
    trajectory_signature[j,12] = seke
    
    
    # temp gradient
    dT_dt = temp_with_time(d[j]['temp'],d[j]['dt'])
    dT_dt_m = np.nanmean(dT_dt)
    trajectory_signature[j,13] = dT_dt_m
    trajectory_signature[j,14] = dT_dt_m/umean
    trajectory_signature[j,15] = dT_dt_m/vmean

    # absolute velocities
    trajectory_signature[j,16] = np.nanmean(np.abs(u))
    trajectory_signature[j,17] = np.nanmean(np.abs(v))
    trajectory_signature[j,18] = np.nanvar(np.abs(u))
    trajectory_signature[j,19] = np.nanvar(np.abs(v))

inds = [0,1,2,3,4,5,8,9,10,11,12]    
#trajectory_signature = trajectory_signature[:,inds]
# =============================================================================
# Separate train and val data
# =============================================================================

X_trn = np.array(list(trajectory_signature[i,:] for i in trn_idx))
X_val = np.array(list(trajectory_signature[i,:] for i in val_idx))

y_trn =  np.array(list(y[i,:] for i in trn_idx))
y_val =  np.array(list(y[i,:] for i in val_idx))


# =============================================================================
# Use GPy method 
# =============================================================================

from GPmethod import *
from sklearn import preprocessing

# =============================================================================
# Remove nans and scale inputs for better stability
# =============================================================================
keep_inds = [~np.isnan(X_trn).any(axis=1)]
X_trn = X_trn[keep_inds]
y_trn = y_trn[keep_inds]

X_scaled = preprocessing.scale(X_trn)
print(X_scaled.shape)
# =============================================================================
# TRAIN MODEL
# =============================================================================
m,kern = TrainModel(X_scaled,y_trn)


# =============================================================================
# MAKE PREDICTION
# =============================================================================

from get_trajectory_signature import *
with open('lagrangian_extra.json') as infile:
    d = json.load(infile)

X_val,y_val,characteristics=get_trajectory_signature(d)
keep_inds = [~np.isnan(X_val).any(axis=1)]
X_val = X_val[keep_inds]
y_val = y_val[keep_inds]
X_val_scaled = preprocessing.scale(X_val)
print(X_val_scaled.shape)

y_pred,gp_err = TestModel(m,X_val_scaled) 


# =============================================================================
# SAVE OUTPUT
# =============================================================================
print('pred')
print(y_pred)
print(gp_err.shape)
print(y_pred.shape)
print(y_val)
pred_lon = y_pred[:,0]
pred_lat = y_pred[:,1]
err_lon = gp_err[:,0]
err_lat = gp_err[:,1]

print(pred_lon)


print(pred_lat)

all_output = np.array((pred_lon,pred_lat,err_lon,err_lat))
np.savetxt("output_prediction.csv", all_output, delimiter=",")


