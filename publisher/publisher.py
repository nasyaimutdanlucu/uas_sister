import requests, uuid, random, time, os
from datetime import datetime

URL = os.getenv("TARGET_URL")

for i in range(1000):
    eid = random.choice([str(uuid.uuid4()), "DUPLICATE-ID"])
    event = {
        "topic": "orders",
        "event_id": eid,
        "timestamp": datetime.utcnow().isoformat(),
        "source": "publisher",
        "payload": {"i": i}
    }
    requests.post(URL, json=[event])
    time.sleep(0.01)