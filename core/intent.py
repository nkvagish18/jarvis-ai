import re


class Intent:

    @staticmethod
    def detect(command):

        command = command.lower().strip()

        # ---------------- Shutdown ----------------

        if re.search(r"\b(shutdown|exit|quit|goodbye|bye)\b", command):
            return "shutdown"

        # ---------------- Apps ----------------

        app_keywords = [
            "notepad",
            "calculator",
            "calc",
            "paint",
            "cmd",
            "command prompt",
            "terminal",
            "explorer",
            "file explorer"
        ]

        if "open" in command and any(app in command for app in app_keywords):
            return "apps"

        # ---------------- Weather ----------------

        weather_words = [
            "weather",
            "temperature",
            "forecast",
            "humidity",
            "rain",
            "wind",
            "climate"
        ]

        if any(word in command for word in weather_words):
            return "weather"

        # ---------------- YouTube ----------------

        youtube_words = [
            "youtube",
            "play",
            "song",
            "music",
            "video",
            "trailer"
        ]

        if any(word in command for word in youtube_words):
            return "youtube"

        # ---------------- Google ----------------

        google_words = [
            "search",
            "google",
            "latest",
            "news",
            "today",
            "current",
            "price",
            "score"
        ]

        if any(word in command for word in google_words):
            return "google"

        # ---------------- Wikipedia ----------------

        wiki_prefixes = (
            "who is",
            "tell me about",
            "history of",
            "biography of",
            "capital of"
        )

        if command.startswith(wiki_prefixes):
            return "wikipedia"

        # ---------------- System ----------------

        if "time" in command or "date" in command:
            return "system"

        # ---------------- Gemini ----------------

        return "gemini"