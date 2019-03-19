import numpy as np
def get_velocity(lat,lon,dt):
    lat = np.array(lat)
    lon = np.array(lon)
    v = (lat[0:-1]-lat[1:])/dt
    u = (lon[0:-1]-lon[1:])/dt
    uv = (u,v)
    return(uv)
