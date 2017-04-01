#!/usr/bin/python
import time
import os
os.system('echo \"none\" > /sys/class/leds/led0/trigger')
while 1:
  i=0
  print("Hello LED is ON "+str(i+1)+"times")
  for i in range(10):
    os.system('echo \"255\" > /sys/class/leds/led0/brightness')
    time.sleep(0.2)
    os.system('echo \"0\" > /sys/class/leds/led0/brightness')
    time.sleep(0.2)
  time.sleep(10)
