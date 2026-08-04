import requests
from core.parser import Parser


class WikipediaService:

    @staticmethod
    def search(command):

        query = Parser.extract_wikipedia_query(command)

        print(f"[Wikipedia] {query}")

        url = (
            f"https://en.wikipedia.org/api/rest_v1/page/summary/"
            f"{query.replace(' ', '_')}"
        )

        try:
            response = requests.get(
                url,
                headers={
                    "User-Agent": "JarvisAI/1.0"
                },
                timeout=10
            )

            if response.status_code != 200:
                return "I couldn't find anything on Wikipedia."

            data = response.json()

            if "extract" in data:
                return data["extract"]

            return "I couldn't find anything on Wikipedia."

        except Exception as e:
            logger.error("Wikipedia", e)
            return (
                "I couldn't find information about that topic."
            )