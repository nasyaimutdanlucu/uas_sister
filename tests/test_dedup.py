def test_deduplication(client):
    event = {
        "topic": "order",
        "event_id": "evt-dup",
        "timestamp": "2025-01-01T10:00:00Z",
        "source": "test",
        "payload": {"x": 1}
    }

    client.post("/publish", json=[event, event, event])

    res = client.get("/events?topic=order")
    assert len(res.json()) == 1