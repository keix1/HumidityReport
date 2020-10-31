# HumidityReport
Raspberry pi report humidity via voice and spreadsheet.

Youtube:

[![](http://img.youtube.com/vi/sFIhbprd-8A/0.jpg)](http://www.youtube.com/watch?v=sFIhbprd-8A "")


## Environment

- Raspberry pi 3B
- Humidity and Temperature sensor: DHT22(AM2302)

## How to use

### Alart about humidity

`python3 humidity_alart.py`

### Logging to Google SpreadSheet

1. Create new Spread Sheet
2. Open Script Editor
3. Write spread_sheet.js
4. Write .env spread sheet url key
5. `python3 sensor_collector.py`

## Reference

[温度/湿度センサーDHT22をRaspberry Piで使用する方法](http://blog.livedoor.jp/victory7com/archives/48343379.html)
