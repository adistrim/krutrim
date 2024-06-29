from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chat import ChatSession

router = APIRouter()

class Message(BaseModel):
    role: str
    content: str

@router.post("/chat/")
async def chat_endpoint(message: Message):
    session = ChatSession()
    reply = await session.get_response(message.content)
    return {"reply": reply}
