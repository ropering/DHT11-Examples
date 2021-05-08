# Operational Test

import datetime
import Adafruit_DHT as dht
from time import sleep

while(1):
    hum,temp = dht.read_retry(dht.DHT11, 4)
    print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temp, hum))
    sleep(1)