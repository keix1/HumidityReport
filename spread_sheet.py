import requests
import os
from dotenv import load_dotenv
load_dotenv()

SHEET_URL = os.environ.get('SHEET_URL')

def post_sensor_to_spreadsheet(humidity, temperature):
    url = f"https://script.google.com/macros/s/{SHEET_URL}/exec?humidity={humidity}&temperature={temperature}"
    requests.get(url)
