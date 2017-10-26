import math
import numpy as np

def Mercator(data):
    #data массив точек. Каждая строка это пара [E,N] и менно в таком виде
    start_latitude = data[1]
    phi = start_latitude*np.pi/180 #start_latitude - широта с которой мы начинаем трек
    R_equator = 6378137.0
    s = cos(phi)
    R = R_equator * 1 * (0.99832407 + 0.00167644 * cos(2 * phi) - 0.00000352*cos(4 * phi))
	
    x_meters = s * R * np.pi * data[:,1] / 180
    y_meters = s * R * np.log(np.tan(np.pi * (90 + data[:,0]) / 360))
    return [x_meters, y_meters]
