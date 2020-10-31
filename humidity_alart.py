# coding: utf-8
import Adafruit_DHT as DHT
import time

import jtalk
import spread_sheet
import humidity_sensor

while True:

    try:
        h, t = humidity_sensor.read_humidity_and_temperature()

        print("Temp= {0:0.1f} deg C" . format(t))
        print("Humidity= {0:0.1f} %" . format(h))

        alart_flag = humidity_sensor.recommend_action(h, t)
        if alart_flag:
            humidity_sensor.voice_humidity_and_temperature(h, t)

    except Exception as e:
        print(e)

    seconds = 30 
    time.sleep(seconds)

