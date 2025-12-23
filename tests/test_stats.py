def test_stats_consistency(client):
    stats = client.get("/stats").json()
    assert stats["received"] >= stats["unique_processed"]
    assert stats["received"] >= stats["duplicate_dropped"]