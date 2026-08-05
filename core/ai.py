import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


class AI:

    def __init__(self):

        genai.configure(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    # ---------------- Normal Chat ----------------

    def ask(self, prompt):

        try:

            response = self.model.generate_content(prompt)

            return response.text.strip()

        except Exception as e:

            print(f"[Gemini Error] {e}")

            return (
                "I'm sorry, I couldn't process your request right now."
            )

    # ---------------- JSON Extraction ----------------

    def extract_json(self, prompt):

        try:

            response = self.model.generate_content(prompt)

            text = response.text.strip()

            # Remove markdown fences if Gemini adds them
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

            return json.loads(text)

        except Exception as e:

            print(f"[Gemini JSON Error] {e}")

            return {}