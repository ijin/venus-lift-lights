#! /usr/bin/env python

import grovepi
import time
import memcache

from subprocess import call

from grove_rgb_lcd import *

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

b=4
grovepi.pinMode(b,"OUTPUT")

time.sleep(1)

def short():
  grovepi.digitalWrite(b,1)
  time.sleep(0.01)
  grovepi.digitalWrite(b,0)
  grovepi.digitalWrite(b,0)

def long():
  grovepi.digitalWrite(b,1)
  time.sleep(0.1)
  grovepi.digitalWrite(b,0)
  grovepi.digitalWrite(b,0)

def pause():
  time.sleep(0.1)


while True:
  ttl = mc.get('sound_ttl')
  sound = mc.get('sound')
  if (sound == 'init') and (ttl != 'yes'):
    print('playing init!')
    mc.set('sound_ttl', 'yes', 2.9)
    setText("Initialize")
    setRGB(0,128,64)
    short()
    pause()
    short()
  elif (sound == 'power') and (ttl != 'yes'):
    print('playing init!')
    mc.set('sound_ttl', 'yes', 2.9)
    setText("Power!!")
    setRGB(0,64,128)
    pause()
    short()
  elif (sound == 'reset') and (ttl != 'yes'):
    print('playing init!')
    mc.set('sound_ttl', 'yes', 2.9)
    long()
    setRGB(0,0,0)
  elif (sound == 'wo') and (ttl != 'yes'):
    print('playing wo!')
    mc.set('sound_ttl', 'yes', 2.9)
    setText("Wave Out")
    setRGB(255,0,0)
    short()
    pause()
    short()
    pause()
    short()
    pause()
  elif (sound == 'wi') and (ttl != 'yes'):
    print('playing wi!')
    mc.set('sound_ttl', 'yes', 2.9)
    setText("Wave In")
    setRGB(0,0,255)
    long()
  elif (sound == 'ready') and (ttl != 'yes'):
    print('playing init!')
    mc.set('sound_ttl', 'yes', 2.9)
    setText("Ready!")
    #setRGB(0,255,0)
    long()
    pause()
    short()
    pause()
    short()
  time.sleep(0.1)
