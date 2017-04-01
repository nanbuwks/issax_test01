#!/usr/bin/python
import time
import os
os.system('echo \"none\" > /sys/class/leds/led0/trigger')
while 1:
  print("Hello LED is ON")
  os.system('echo \"255\" > /sys/class/leds/led0/brightness')
  time.sleep(10)
  print("Hello LED is OFF")
  os.system('echo \"0\" > /sys/class/leds/led0/brightness')
  time.sleep(10)

