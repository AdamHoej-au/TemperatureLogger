import os
import time
import csv
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
try: 
	f = open('/home/pi/humidityLog.csv','a+')
	if os.stat('home/pi/humidityLog.csv').st_size==0:
		f.write('Date,Time,Temperature,Humidity\r\n')
		f.flush()
except:
	pass

while True:
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR,DHT_PIN)
	if humidity is not None and temperature is not None:
		f.write('{0},{1},{2:0.1f},{3:0.1f}\r\n'.format(time.strftime('%y/%m/%d'),time.strftime('%H:%M:%S'), temperature,humidity))
		f.flush()
	else:
		print("Nej.")

	time.sleep(30)

