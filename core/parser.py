import re


class Parser:

    @staticmethod
    def extract_google_query(command):

        command = command.lower()

        patterns = [
            r"search (.+)",
            r"google (.+)",
            r"find (.+)",
            r"look up (.+)"
        ]

        for pattern in patterns:
            match = re.search(pattern, command)
            if match:
                return match.group(1).strip()

        return command


    @staticmethod
    def extract_youtube_query(command):

        command = command.lower()

        patterns = [
            r"play (.+)",
            r"youtube (.+)",
            r"search youtube (.+)"
        ]

        for pattern in patterns:
            match = re.search(pattern, command)
            if match:
                return match.group(1).strip()

        return command


    @staticmethod
    def extract_wikipedia_query(command):

        command = command.lower()

        prefixes = [
            "who is",
            "tell me about",
            "history of",
            "biography of",
            "capital of"
        ]

        for prefix in prefixes:
            if command.startswith(prefix):
                return command.replace(prefix, "").strip()

        return command


    @staticmethod
    def extract_weather_city(command):

        command = command.lower()

        match = re.search(r"weather in (.+)", command)

        if match:
            return match.group(1).strip()

        return None

    @staticmethod
    def extract_weather_city(command):

        command = command.lower().strip()

        prefixes = [
            "weather in",
            "temperature in",
            "forecast for",
            "forecast in"
        ]

        for prefix in prefixes:
            if command.startswith(prefix):
                return command.replace(prefix, "").strip().title()

        return None

    @staticmethod
    def extract_news_category(command):

        command = command.lower()

        if "technology" in command:
            return "technology"

        if "sports" in command:
            return "sports"

        if "business" in command:
            return "business"

        if "health" in command:
            return "health"

        if "science" in command:
            return "science"

        return "general"

    