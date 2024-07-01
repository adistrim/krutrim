import uuid
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chat import ChatSession
from app.firebase.firebase import add_chat_message

router = APIRouter()

class Message(BaseModel):
    session_id: str
    role: str
    content: str

@router.post("/chat/")
async def chat_endpoint(message: Message):
    session = ChatSession()
    reply = await session.get_response(message.content)
    
    # Save user message to Firebase
    add_chat_message(message.session_id, message.role, message.content)
    
    # Save assistant reply to Firebase
    add_chat_message(message.session_id, 'assistant', reply)
    
    return {"reply": reply}

@router.get("/generate_session_id/")
async def generate_session_id():
    session_id = str(uuid.uuid4())
    return {"session_id": session_id}
