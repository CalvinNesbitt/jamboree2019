import numpy as np
# =============================================================================
# GET DATA
# =============================================================================

output = np.loadtxt('output_prediction.csv',delimiter=",")
print(output.shape)


pred_lon = output[0,:]
pred_lat = output[1,:]
err_lon = output[2,:]
err_lat = output[3,:]

print("Predicted Longitudes")
print(pred_lon)
print("1 Sigma on Longitudes")
print(err_lon)
print("Predicted Latitudes")
print(pred_lat)
print("1 Sigma on Latitudes")
print(err_lat)

