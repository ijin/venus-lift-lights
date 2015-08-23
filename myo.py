#!/usr/bin/python
''' DON'T TOUCH THESE FIRST LINES! '''
''' ============================== '''
from PyoConnect import *
myo = Myo(sys.argv[1] if len(sys.argv) >= 2 else None) 
''' ============================== '''

# Edit here:

import time
import memcache
from urllib import urlopen

def onPoseEdge(pose, edge):
    mc = memcache.Client(['127.0.0.1:11211'], debug=0)
    if (pose == 'fist'):
        mc.set('pose', 'fist', 3)
        mc.set('edge', edge, 3)
        print("FIST: "+pose+", "+edge)
    elif (pose == 'fingersSpread'):
        mc.set('pose', 'fingersSpread', 3)
        mc.set('edge', edge, 3)
        print("FINGERS: "+pose+", "+edge)
    elif (pose == 'waveIn'):
        mc.set('pose', 'waveIn', 3)
        mc.set('edge', edge, 3)
        print("WAVE_IN: "+pose+", "+edge)
    elif (pose == 'waveOut'):
        mc.set('pose', 'waveOut', 3)
        mc.set('edge', edge, 3)
        print("WAVE_OUT: "+pose+", "+edge)
    else:
        mc.set('pose', pose)
        mc.set('edge', edge)
        print("onPoseEdge: "+pose+", "+edge)
    sys.stdout.flush()

def onPeriodic():
    return



# Stop editting

myo.onPoseEdge = onPoseEdge
myo.onPeriodic = onPeriodic

''' DON'T TOUCH BELOW THIS LINE! '''
''' ============================ '''
myo.connect()
m = memcache.Client(['127.0.0.1:11211'], debug=0)
m.set('sound', 'init', 1)
while True:
    myo.run(1)
    myo.tick()

