# coding: utf-8
import Adafruit_DHT as DHT
import time

import jtalk
import spread_sheet
import humidity_sensor

while True:

    try:
        ## 測定開始
        h, t = humidity_sensor.read_humidity_and_temperature()

        ## 結果表示
        print("Temp= {0:0.1f} deg C" . format(t))
        print("Humidity= {0:0.1f} %" . format(h))

        spread_sheet.post_sensor_to_spreadsheet(humidity=str(round(h, 1)), temperature=str(round(t, 1)))
    except:
        pass

    seconds = 30 
    time.sleep(seconds)




