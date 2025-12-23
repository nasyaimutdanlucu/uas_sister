import threading

def send(client, event):
    client.post("/publish", json=[event])

def test_concurrent_publish(client):
    event = {
        "topic": "race",
        "event_id": "evt-race",
        "timestamp": "2025-01-01T10:00:00Z",
        "source": "test",
        "payload": {}
    }

    threads = []
    for _ in range(5):
        t = threading.Thread(target=send, args=(client,event))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    res = client.get("/events?topic=race")
    assert len(res.json()) == 1