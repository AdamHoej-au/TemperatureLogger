#!/usr/bin/env python
# Found at https://www.raspberrypi.org/forums/viewtopic.php?t=128776
import glob
import os
import time

# DS18B20.py
# 2016-04-25
# Public Domain

# Typical reading
# 73 01 4b 46 7f ff 0d 10 41 : crc=41 YES
# 73 01 4b 46 7f ff 0d 10 41 t=23187
# sensors = glob.glob("/sys/bus/w1/devices/28-00*/w1_slave")
sensors = {"28-00000846c002":"Johnny", "28-0000084718f2":"Allan"}
logPath = {"/Logfiles/"}

print(sensors)
    
while True:
   for sensor in sensors:
    # for idx, val in enumerate(sensornames):
    #    print(idx,val)
    # id = sensor.split("/")[5]
    id = sensors.get(sensor)
    try:
        f = open(sensor, "r")
        data = f.read()
        f.close()
        if "YES" in data:
            (discard, sep, reading) = data.partition(' t=')
            t = float(reading) / 1000.0
            print("{},{},{},{:.1f}".format(time.strftime('%y/%m/%d'),time.strftime('%H:%M:%S'),id, t))
        else:
            print("999.9")

    except:
        pass

    time.sleep(3.0)




# import time
# import csv
# import Adafruit_DHT

# DHT_SENSOR = Adafruit_DHT.DHT11
# DHT_PIN = 4
# try: 
# 	f = open('/home/pi/humidityLog.csv','a+')
# 	if os.stat('home/pi/humidityLog.csv').st_size==0:
# 		f.write('Date,Time,Temperature,Humidity\r\n')
# 		f.flush()
# except:
# 	pass

# while True:
# 	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR,DHT_PIN)
# 	if humidity is not None and temperature is not None:
# 		f.write('{0},{1},{2:0.1f},{3:0.1f}\r\n'.format(time.strftime('%y/%m/%d'),time.strftime('%H:%M:%S'), temperature,humidity))
# 		f.flush()
# 	else:
# 		print("Nej.")

# 	time.sleep(30)
