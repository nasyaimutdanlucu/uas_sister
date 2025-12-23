import os
import time
import requests

URL = os.getenv("AGGREGATOR_URL", "http://aggregator:8080/publish")

event = {
    "service": "publisher",
    "message": "hello world"
}

for i in range(10):  # coba 10x
    try:
        print(f"Trying to connect... attempt {i+1}")
        requests.post(URL, json=[event], timeout=3)
        print("Publish success")
        break
    except Exception as e:
        print("Aggregator not ready, retrying...", e)
        time.sleep(2)