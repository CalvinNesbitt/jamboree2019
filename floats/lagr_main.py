#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 10:36:13 2019

@author: sr3117
"""

# =============================================================================
# Start message
# =============================================================================
print('start')
print("Ma l'uomo grida dovunque la sorte d'una patria")
print(' ')

# =============================================================================
# Packages
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np
import time

import json
import plotter

tic = time.time()

# =============================================================================
# Directories 
# =============================================================================
#Main directory path
mdir = "/Users/sr3117/Desktop/Jambo2019/data/"

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

with open(mdir + '/lagrangian.json') as infile:
    d = json.load(infile)

d_trn = list(d[i] for i in val_idx)
d_val = list(d[i] for i in trn_idx)

# =============================================================================
# Open data
# =============================================================================
data = d_trn[0]
X = data['lon']
Y = data['lat']
T = data['temp']

# =============================================================================
# Plot
# =============================================================================
tmp = T
fig,ax = plt.subplots()
ax.plot(X,Y)

# =============================================================================
# Farewell message
# =============================================================================
plt.show()
toc = time.time()-tic
print(" ")
print("elapsed time = %.3f" % toc)
print("end") 