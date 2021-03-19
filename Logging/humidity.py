import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
while True:
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR,DHT_PIN)
	if humidity is not None and temperature is not None:
		print("Temperatur:{0:0.1f}*C Fugtighed:{1:0.1f}%".format(temperature,humidity))
	else:
		print("Hallo! Sensorfejl!")
