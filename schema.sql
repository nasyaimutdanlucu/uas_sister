CREATE TABLE processed_events (
    id BIGSERIAL PRIMARY KEY,
    topic TEXT NOT NULL,
    event_id TEXT NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL,
    source TEXT NOT NULL,
    payload JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    UNIQUE (topic, event_id)
);

CREATE TABLE stats (
    key TEXT PRIMARY KEY,
    value BIGINT NOT NULL
);

INSERT INTO stats (key, value) VALUES
('received', 0),
('unique_processed', 0),
('duplicate_dropped', 0);