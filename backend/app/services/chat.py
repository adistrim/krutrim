from openai import OpenAI
from app.core.config import settings

class ChatSession:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.krutrim_api_key,
            base_url=settings.krutrim_base_url
        )
        self.messages = [{"role": "system", "content": "You are a helpful assistant."}]
        self.chat_history = []

    async def get_response(self, user_message: str):
        self.messages.append({"role": "user", "content": user_message})
        response = self.client.chat.completions.create(
            model="Krutrim-spectre-v2",
            messages=self.messages
        )
        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        self.chat_history.append({"role": "user", "content": user_message})
        self.chat_history.append({"role": "assistant", "content": reply})
        return reply
