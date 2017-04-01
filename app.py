#!/usr/bin/python
import time
import os
os.system('echo \"none\" > /sys/class/leds/led0/trigger')
while 1:
  for j in range(10):
    print("Hello LED is ON "+str(j+1)+"times")
    for i in range(j):
      os.system('echo \"255\" > /sys/class/leds/led0/brightness')
      time.sleep(0.2)
      os.system('echo \"0\" > /sys/class/leds/led0/brightness')
      time.sleep(0.2)
    time.sleep(10)
