#Transfer data from gateway to server

import requests
import json
import time

url="http://127.0.0.1:8000/Transdata"

while(True):
    payload = ""
    response = requests.post(url, payload)
    #print(response)
    time.sleep(1)