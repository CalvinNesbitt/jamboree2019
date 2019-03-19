import json
import numpy as np
import matplotlib.pyplot as plt
# =============================================================================
# Random seed: separate train and validation
# =============================================================================
np.random.seed(seed = 0)
val_idx = []
for i in range(100):
      r=np.random.randint(0,600)
      if r not in val_idx: val_idx.append(r)
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


from velocity import get_velocity

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

# =============================================================================
# TRAIN MODEL
# =============================================================================
m,kern = TrainModel(X_scaled,y_trn)


keep_inds = [~np.isnan(X_val).any(axis=1)]
X_val = X_val[keep_inds]
y_val = y_val[keep_inds]
X_val_scaled = preprocessing.scale(X_val)

# =============================================================================
# MAKE PREDICTION
# =============================================================================
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
true_lon = y_val[:,0]
true_lat = y_val[:,1]

print(pred_lon)
print(true_lon)


print(pred_lat)
print(true_lat)

all_output = np.array((pred_lon,pred_lat,err_lon,err_lat,true_lon,true_lat))
print(all_output.shape)
np.savetxt("output.csv", all_output, delimiter=",")
