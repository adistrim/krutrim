from fastapi import WebSocket, WebSocketDisconnect
from app.services.chat import ChatSession

sessions = {}

async def websocket_endpoint(websocket: WebSocket, session_id: str):
    await websocket.accept()
    if session_id not in sessions:
        sessions[session_id] = ChatSession()
    session = sessions[session_id]

    try:
        while True:
            data = await websocket.receive_text()
            reply = await session.get_response(data)
            await websocket.send_text(reply)
    except WebSocketDisconnect:
        del sessions[session_id]
