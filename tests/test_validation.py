def test_invalid_event_schema(client):
    bad_event = {
        "topic": "order",
        "event_id": "evt-bad"
        # timestamp hilang
    }

    res = client.post("/publish", json=[bad_event])
    assert res.status_code == 422