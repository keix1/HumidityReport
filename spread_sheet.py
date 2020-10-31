import requests

def post_sensor_to_spreadsheet(humidity, temperature):
    url = f"https://script.google.com/macros/s/xxxxxxxxx/exec?humidity={humidity}&temperature={temperature}"
    requests.get(url)
