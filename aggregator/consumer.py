import os, json, asyncio
import asyncpg
import redis.asyncio as redis

DATABASE_URL = os.getenv("DATABASE_URL")
BROKER_URL = os.getenv("BROKER_URL")

async def consumer():
    pool = await asyncpg.create_pool(DATABASE_URL)
    r = redis.from_url(BROKER_URL)

    while True:
        _, raw = await r.blpop("event_queue")
        event = json.loads(raw)

        async with pool.acquire() as conn:
            async with conn.transaction(isolation="read_committed"):
                result = await conn.execute("""
                    INSERT INTO processed_events
                    (topic, event_id, timestamp, source, payload)
                    VALUES ($1, $2, $3, $4, $5)
                    ON CONFLICT (topic, event_id) DO NOTHING
                """,
                event["topic"],
                event["event_id"],
                event["timestamp"],
                event["source"],
                json.dumps(event["payload"])
                )