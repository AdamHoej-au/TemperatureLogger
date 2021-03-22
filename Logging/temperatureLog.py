#!/usr/bin/env python
# Found at https://www.raspberrypi.org/forums/viewtopic.php?t=128776
import glob
import time

# DS18B20.py
# 2016-04-25
# Public Domain

# Typical reading
# 73 01 4b 46 7f ff 0d 10 41 : crc=41 YES
# 73 01 4b 46 7f ff 0d 10 41 t=23187
sensors = glob.glob("/sys/bus/w1/devices/28-00*/w1_slave")
sensornames = {"Johnny", "Allan", "Lars"}

print(sensors)
    
while True:
   for sensor in sensors:
    # for idx, val in enumerate(sensornames):
    #    print(idx,val)
    id = sensor.split("/")[5]
    try:
        f = open(sensor, "r")
        data = f.read()
        f.close()
        if "YES" in data:
            (discard, sep, reading) = data.partition(' t=')
            t = float(reading) / 1000.0
            print("{0} {1:.1f}".format(id, t))
        else:
            print("999.9")

    except:
        pass

   time.sleep(3.0)