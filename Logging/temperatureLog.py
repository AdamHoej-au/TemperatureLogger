import time

sensors = {"28-00000846c002": 0, "28-0000084718f2": 0}

while 1:
    for sensor in sensors:
        tempfile = open("/sys/bus/w1/devices/{0}/w1_slave".format(sensor))
        temptext = tempfile.read()
        tempfile.close()
        tempcelsius = temptext.split("\n")[1].split(" ")[9]
        temperature = float(tempcelsius[2:])
        temperature = temperature / 1000
        sensors[sensor] = temperature
    print(' ').join(['{0:2.4f},'.format(v) for k, v in sensors.iteritems()])
