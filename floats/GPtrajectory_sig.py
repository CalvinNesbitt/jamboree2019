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

characteristics = ['mean u','mean v','var u','var v','x dist','y dist','mean temp','mean var']
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
    # distance travelled in x and y 
    trajectory_signature[j,4]=np.sum(np.array(d[j]['lon']))
    trajectory_signature[j,5]=np.sum(np.array(d[j]['lat']))
    # mean and var temp
    trajectory_signature[j,6] = np.mean(np.array(d[j]['temp']))
    trajectory_signature[j,7] = np.var(np.array(d[j]['temp']))


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
