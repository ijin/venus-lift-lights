#! /usr/bin/env python

import time
import grovepi

import memcache

import subprocess
import sys

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

button = 3
grovepi.pinMode(button,"INPUT") 

#cmd = ["ls", "-l"]
cmd = "sudo supervisorctl restart myo"

while True:
  ttl = mc.get('ttl2')
  b = grovepi.digitalRead(button)
  #print b
  #print ttl
  if (b == 1):
    if (ttl == 'yes'):
      print('button pressed too fast: ' + str(time.time()))
    else:
      mc.set('ttl2', 'yes', 2)
      mc.set('sound', 'reset', 2)
      print('button pressed! ' + str(time.time()))
      sys.stdout.flush()
      subprocess.call(cmd, shell=True)
  time.sleep(0.1)
  sys.stdout.flush()

