from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
import asyncio, json

app = FastAPI()
clients = set()

class Metrics(BaseModel):
    camera: str
    ts: float
    density: float
    grid_counts: list
    avg_flow: list

@app.post("/ingest")
async def ingest(m: Metrics):
    data = m.dict()
    # broadcast to connected clients
    for ws in list(clients):
        try:
            await ws.send_json(data)
        except:
            clients.remove(ws)
    return {"status": "ok"}

@app.websocket("/ws/live")
async def ws_live(ws: WebSocket):
    await ws.accept()
    clients.add(ws)
    try:
        while True:
            await asyncio.sleep(10)
    except:
        clients.remove(ws)
