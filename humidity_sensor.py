# coding: utf-8
import Adafruit_DHT as DHT
import time

import jtalk
import spread_sheet


def read_humidity_and_temperature():
    ## センサーの種類
    SENSOR_TYPE = DHT.DHT22

    ## 接続したGPIOポート
    DHT_GPIO = 4

    ## 測定開始
    h,t = DHT.read_retry(SENSOR_TYPE, DHT_GPIO)
    
    return h, t

def voice_humidity_and_temperature(humidity, temperature):
    jtalk.jtalk(f'湿度{round(humidity, 1)}パーセント、気温は{round(temperature, 1)}度です')
    time.sleep(6)

def recommend_action(humidity, temperature):
    if humidity < 57:
        jtalk.jtalk(f'乾燥に気をつけてください')
        time.sleep(1.5)
        return True
    elif humidity > 68:
        jtalk.jtalk(f'湿度が高すぎるとカビがはえますよ')
        time.sleep(1.5)
        return True
    return False



if __name__=='__main__':
    h, t = read_humidity_and_temperature()
    print(f'湿度：{round(h, 1)}%')
    print(f'温度：{round(t, 1)}度')
    voice_humidity_and_temperature(h, t)
    recommend_action(h, t)

