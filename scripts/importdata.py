from __future__ import print_function

import glob
import numpy as np

import yaml
import gzip
import os


def getCoords(senseFrame):
    return [senseFrame['east'],
            senseFrame['nord']]


def getSteering(senseFrame):
    return [senseFrame['steeringAngle']]


def processFile(filename):
    print(filename)
    resultFolder = 'result/' + filename.split('\\')[0] + '/'
    resultName = filename.split('\\')[1] + '.csv'
    print(resultFolder)
    if not os.path.exists(resultFolder):
        os.makedirs(resultFolder)


    lines = gzip.GzipFile(filename).readlines()
    
    good_lines = '\n'.join(lines[1:])
    good_lines = good_lines.replace(':', ' : ')
    yaml_data = yaml.load(good_lines)
    
    shots = yaml_data['shots']
    sense1 = [getCoords(shot['sense1']['senseData'])
              for shot in shots if 'sense1' in shot.keys()]

    steering = [getSteering(shot['dbwFbVehicleCan']['vehicleCanData']['vehicleCanDetection0'])
              for shot in shots if 'dbwFbVehicleCan' in shot.keys()]

    coords = np.array(sense1)
    steering = np.array(steering)

    if(coords.shape[0] != steering.shape[0]):
        
        xp = range(steering.shape[0])
        fp = np.array(steering[:, 0])

        steering = np.array([np.interp(range(coords.shape[0]), xp, fp)]).T

    print(coords.shape)
    print(steering.shape)

    result = np.concatenate((np.array(sense1), np.array(steering)), axis=1)
    np.savetxt(resultFolder + resultName, result, delimiter=",")



files = glob.glob('*/*.gz')

for f in files:
    processFile(f)






