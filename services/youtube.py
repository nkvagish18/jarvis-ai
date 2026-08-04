import webbrowser
from core.parser import Parser


class YouTubeService:

    @staticmethod
    def search(command):

        query = Parser.extract_youtube_query(command)

        try:
            print(f"[YouTube] {query}")

            webbrowser.open(
                f"https://www.youtube.com/results?search_query={query}"
            )

            return f"Searching YouTube for {query}"

        except Exception as e:
            logger.error("Youtube", e)
            return (
                "I couldn't open YouTube right now."
            )