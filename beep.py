#! /usr/bin/env python

import mraa
import time
import memcache

from subprocess import call

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

b=mraa.Gpio(7)
b.dir(mraa.DIR_OUT)

time.sleep(1)

def short():
  b.write(1)
  time.sleep(0.01)
  b.write(0)

def long():
  b.write(1)
  time.sleep(0.1)
  b.write(0)

def pause():
  time.sleep(0.1)


while True:
  ttl = mc.get('sound_ttl')
  sound = mc.get('sound')
  if (sound == 'init') and (ttl != 'yes'):
    print('playing init!')
    mc.set('sound_ttl', 'yes', 2.9)
    short()
    pause()
    short()
  elif (sound == 'power') and (ttl != 'yes'):
    print('playing init!')
    mc.set('sound_ttl', 'yes', 2.9)
    pause()
    long()
  elif (sound == 'reset') and (ttl != 'yes'):
    print('playing init!')
    mc.set('sound_ttl', 'yes', 2.9)
    short()
  time.sleep(0.1)
