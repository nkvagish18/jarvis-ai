import webbrowser
from core.parser import Parser
from utils.logger import logger

class SearchService:

    @staticmethod
    def google(command):

        query = Parser.extract_google_query(command)

        try:
            logger.info(f"[Google Search] {query}")
            webbrowser.open(
                f"https://www.google.com/search?q={query}"
            )

            return f"Searching Google for {query}"
        
        except Exception as e:
            logger.error("Google Search", e)
            return (
                "I couldn't perform the Google search right now."
            )