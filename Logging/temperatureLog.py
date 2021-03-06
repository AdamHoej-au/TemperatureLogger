#!/usr/bin/env python
# Found at https://www.raspberrypi.org/forums/viewtopic.php?t=128776
# https://www.raspberrypi.org/forums/viewtopic.php?t=150797
import glob
import os
import glob
import datetime
import time
from time import sleep
from sensorList import sensors

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# DS18B20.py
# 2016-04-25
# Public Domain

# sensors = {}
# sensors["28-00000846c002"] = "Johnny"
# sensors["28-0000084718f2"] = "Allan"
# sensors["28-0000084718f2"] = "Lars"
logPath = '../Logs/'
logFile = 'TemperatureLog.csv'

print(sensors)

try:
	f = open(logPath + logFile,'a+')
	if os.stat(logPath + logFile).st_size==0:
		f.write('Name,Date,Time,Temperature\r\n')
		f.flush()
except:
	pass




while True:
   date_log = str(time.strftime('%y-%m-%d')) + ','
   date_log += str(time.strftime('%H:%M:%S'))
#    print("Next Temp Set")
   def get_temp(device):
      #To read the sensor data, just open the w1_slave file
        f = open(device, 'r')
        data = f.readlines()
        f.close()
        deg_f = ''
        if data[0].strip()[-3:] == 'YES':
            temp = data[1][data[1].find('t=')+2:]
              #If temp is 0 or not numeric an exception
              #will occur so lets handle it gracefully
            try:
                if float(temp) == 0:
                    deg_f = 999.9
                else:
                    deg_f = (float(temp)/1000.00)
            except:
                print("Error with t=", temp)
                pass
        return deg_f

   for sensor in sensors:
        sensor_name = sensors[sensor]  # <-- grabs the sensor name given to it
        with open(logPath + logFile, 'a') as f:
            s = sensor_name + ','
            s += date_log + ','
            # <-- path added here to access sensor
            s += str(get_temp('/sys/bus/w1/devices/' +
                sensor + '/w1_slave')) + '\r\n'
            print(s)
            f.write(s)
            f.flush()
          #When there are multiple devices, a short pause
          #interval between reading sensors seems to work best
        time.sleep(1)

   time.sleep(900)
