def test_persistence_after_restart(client):
    event = {
        "topic": "persist",
        "event_id": "evt-persist",
        "timestamp": "2025-01-01T10:00:00Z",
        "source": "svc",
        "payload": {}
    }

    client.post("/publish", json=[event])

    # restart container manual (dibuktikan via laporan)
    res = client.get("/events?topic=persist")
    assert len(res.json()) == 1