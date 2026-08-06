import json

from google import genai
from utils.logger import logger
from utils.config import Config


class AI:

    def __init__(self):

        self.client = genai.Client(
            api_key=Config.GEMINI_API_KEY
        )

    # ---------------- Normal Chat ----------------

    def ask(self, prompt):

        try:

            response = self.client.models.generate_content(
                model=Config.GEMINI_MODEL,
                contents=prompt
            )

            if not response or not getattr(response, "text", None):
                return "I couldn't generate a response."

            return response.text.strip()

        except Exception as e:

            logger.error(f"[Gemini Error] {e}")

            error = str(e).lower()

            if "503" in error or "unavailable" in error:
                return (
                    "I'm a little busy right now. Please try again in a few seconds."
                )

            if "429" in error:
                return (
                    "I've reached my request limit for now. Please try again later."
                )

            if "401" in error:
                return (
                    "There seems to be an authentication problem with the AI service."
                )

            return (
                "I'm sorry, I couldn't process your request right now."
            )

    # ---------------- JSON Extraction ----------------

    def extract_json(self, prompt):

        try:

            response = self.client.models.generate_content(
                model=Config.GEMINI_MODEL,
                contents=prompt
            )

            text = response.text.strip()

            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

            return json.loads(text)

        except Exception as e:

            logger.error(f"[Gemini JSON Error] {e}")

            return {}

    # ---------------- Context Chat ----------------

    def chat(self, message, conversation=""):

        prompt = f"""
You are Jarvis, an intelligent AI assistant.

Conversation history:

{conversation}

Current user message:

{message}

Answer naturally and conversationally.
"""

        return self.ask(prompt)