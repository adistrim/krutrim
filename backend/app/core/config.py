import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    krutrim_api_key: str = os.getenv("KRUTRIM_API_KEY")
    krutrim_base_url: str = os.getenv("KRUTRIM_URL")

settings = Settings()
