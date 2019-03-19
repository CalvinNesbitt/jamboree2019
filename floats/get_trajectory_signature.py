from velocity import *

def get_trajectory_signature(d):

    characteristics = ['mean u','mean v','var u','var v','variance x','variance y','mean temp','var temp',
                           'direction x', 'direction y','gyration','kinetic energy','standing eddy kinetic energy',
                           'temp gradient with time','temp gradient with time/umean','temp gradientwith time/vmean',
                           'mean |u|','mean|v|','var |u|','var|v|']
    #temp gradient in x and y, speed, overall direction of trajectory,
    N = len(d)
    trajectory_signature = np.zeros((N,len(characteristics)))
    y = np.zeros((N,2))
    for j in range(N):
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



    return(trajectory_signature,y,characteristics)


