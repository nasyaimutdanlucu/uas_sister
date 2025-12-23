def test_idempotent_behavior(client):
    event = {
        "topic": "payment",
        "event_id": "evt-idem",
        "timestamp": "2025-01-01T10:00:00Z",
        "source": "svc",
        "payload": {"amount": 100}
    }

    client.post("/publish", json=[event])
    client.post("/publish", json=[event])

    res = client.get("/events?topic=payment")
    assert len(res.json()) == 1