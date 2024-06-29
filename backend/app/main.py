from fastapi import FastAPI
from app.api.v1.endpoints import chat
from app.api.v1 import websocket

app = FastAPI()

app.include_router(chat.router, prefix="/api/v1")

app.add_api_websocket_route("/ws/{session_id}", websocket.websocket_endpoint)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
