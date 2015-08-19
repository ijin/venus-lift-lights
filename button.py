#! /usr/bin/env python

import mraa
import time

import memcache

import subprocess
import sys

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

x = mraa.Gpio(8)
x.dir(mraa.DIR_IN)
time.sleep(1)

#cmd = ["ls", "-l"]
cmd = ["sudo", "supervisorctl", "restart", "myo"]

while True:
  ttl = mc.get('ttl2')
  b = x.read()
  if (b == 1):
    if (ttl == 'yes'):
      print('button pressed too fast')
    else:
      mc.set('ttl2', 'yes', 2)
      mc.set('sound', 'reset', 2)
      print('button pressed! ' + str(time.time()))
      subprocess.call(cmd, shell=True)
  time.sleep(0.1)
  sys.stdout.flush()

