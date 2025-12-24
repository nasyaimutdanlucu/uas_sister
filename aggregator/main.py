from fastapi import FastAPI
from models import Event
import redis.asyncio as redis
import os, asyncio
from consumer import consumer

app = FastAPI()
r = redis.from_url(os.getenv("BROKER_URL"))

@app.on_event("startup")
async def startup():
    asyncio.create_task(consumer())

@app.post("/publish")
async def publish(events: list[Event]):
    for e in events:
        await r.rpush("event_queue", e.model_dump_json())
    return {"accepted": len(events)}

@app.get("/events")
async def get_events():
    return {"message": "ambil dari DB"}

@app.get("/stats")
async def stats():
    return {"received": 0, "unique_processed": 0}