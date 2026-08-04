import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


class AI:

    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def ask(self, prompt):

        try:

            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:
            logger.error("Gemini", e)
            return (
                "I'm sorry, I couldn't process your request right now. "
                "Please try again in a moment."
            )