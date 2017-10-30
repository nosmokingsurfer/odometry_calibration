import math
import numpy as np

def Mercator(data):
    #data[0] = [east, north]
    start_latitude = data[0][1] #the latitude we start from
    print(start_latitude)
    phi = start_latitude*np.pi/180.0
    R_equator = 6378137.0
    s = np.cos(phi)
    R = R_equator * 1 * (0.99832407 + 0.00167644 * np.cos(2 * phi) - 0.00000352*np.cos(4 * phi))
    
    x_meters = s * R * np.pi * data[:,0] / 180.0
    y_meters = s * R * np.log(np.tan(np.pi * (90.0 + data[:,1]) / 360.0))
    return [x_meters, y_meters]
