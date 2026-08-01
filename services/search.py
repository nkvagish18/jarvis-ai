import webbrowser
from urllib.parse import quote


class SearchService:

    @staticmethod
    def google(command):
        query = command.lower()
        prefixes = [
            "search",
            "google",
            "search for",
            "google search"
        ]
        for prefix in prefixes:
            if query.startswith(prefix):
                query = query.replace(prefix, "", 1).strip()
                break
        if not query:
            return "What would you like me to search?"
        url = f"https://www.google.com/search?q={quote(query)}"
        print(f"[Google Search] {query}")
        webbrowser.open(url)
        return f"Searching Google for {query}"