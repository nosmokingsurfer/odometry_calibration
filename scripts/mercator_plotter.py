from __future__ import absolute_import, unicode_literals
import math
import numpy as np

import glob

import matplotlib.pyplot as plt


def Mercator(data):
    start_latitude = data[0][1]
    print(start_latitude)
    phi = start_latitude*np.pi/180.0
    R_equator = 6378137.0
    s = np.cos(phi)
    R = R_equator * 1 * (0.99832407 + 0.00167644 * np.cos(2 * phi) - 0.00000352*np.cos(4 * phi))
	
    x_meters = s * R * np.pi * data[:,0] / 180.0
    y_meters = s * R * np.log(np.tan(np.pi * (90.0 + data[:,1]) / 360.0))
    return [x_meters, y_meters]


files = glob.glob('*/*.csv')

print(files)

track = []


allLines = [open(f).readlines() for f in files]

allLines = [item for sublist in allLines for item in sublist]

data = []

for l in allLines:
    data.append([float(x) for x in l.split(',')])

data = np.array(data)

meters = Mercator(data)
track.extend(meters)


track = np.array(track)

plt.plot(track[:][0], track[:][1])
plt.grid(True)
plt.axis('equal')
plt.show()