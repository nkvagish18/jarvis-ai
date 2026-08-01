import webbrowser
from urllib.parse import quote


class YouTubeService:

    @staticmethod
    def search(command):

        query = command.lower()

        prefixes = [
            "play",
            "search youtube",
            "youtube",
            "search on youtube"
        ]

        for prefix in prefixes:
            if query.startswith(prefix):
                query = query.replace(prefix, "", 1).strip()
                break

        if not query:
            webbrowser.open("https://youtube.com")
            return "Opening YouTube"

        print(f"[YouTube Search] {query}")

        url = f"https://www.youtube.com/results?search_query={quote(query)}"

        webbrowser.open(url)

        return f"Searching YouTube for {query}"