import requests
import json
import time
import os

url="http://127.0.0.1:8000/Postjson"
path = "./data/"

for filename in os.listdir(path):
    if filename.endswith(".txt") and filename[0] !="@":

        f = open(path + filename, 'rb')
        rows = f.readlines()
        f.close()

        os.rename(path + filename, path + "@" + filename)  #check trensferred data file

        for row in rows:
            payload = row.strip()
            response = requests.post(url, payload)
            #response = requests.post(url,  data=json.dumps(payload))
            #print(response.text) #TEXT/HTML
            time.sleep(1)