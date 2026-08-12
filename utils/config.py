import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # ================= AI =================

    GEMINI_MODEL = "gemini-2.5-flash"

    # ================= Conversation =================

    MAX_CONVERSATION_HISTORY = 10

    # ================= Memory =================

    MEMORY_FILE = "memory/storage.json"

    # ================= APIs =================

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

    NEWS_API_KEY = os.getenv("NEWS_API_KEY")