import numpy as np
# =============================================================================
# GET DATA
# =============================================================================

output = np.loadtxt('output.csv',delimiter=",")
print(output.shape)


pred_lon = output[0,:]
pred_lat = output[1,:]
err_lon = output[2,:]
err_lat = output[3,:]
true_lon = output[4,:]
true_lat = output[5,:]

# =============================================================================
# PLOT RESULTS
# =============================================================================
import matplotlib.pyplot as plt
plt.plot(true_lon,true_lon,'k-')
plt.errorbar(true_lon,pred_lon,yerr=err_lon,fmt='bx')
plt.title('prediction vs truth')
plt.xlabel('true mean longitude')
plt.ylabel('predicted mean longitude')
plt.title('Longitude')
plt.savefig('plots/pred_vs_truth_longitude.png')

plt.clf()
plt.plot(true_lat,true_lat,'k-')
plt.errorbar(true_lat,pred_lat,yerr=err_lat,fmt='bx')
plt.title('prediction vs truth')
plt.xlabel('true mean latitude')
plt.ylabel('predicted mean latitude')
plt.title('Latitude')
plt.savefig('plots/pred_vs_truth_latitude.png')
