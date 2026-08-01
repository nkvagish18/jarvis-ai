import wikipedia


class WikipediaService:

    @staticmethod
    def search(command):

        prefixes = [
            "who is",
            "what is",
            "tell me about",
            "explain"
        ]

        query = command

        for prefix in prefixes:
            if query.lower().startswith(prefix):
                query = query[len(prefix):].strip()
                break

        try:
            page = wikipedia.page(query, auto_suggest=True)

            summary = wikipedia.summary(page.title, sentences=2)

            print(f"[Wikipedia] {page.title}")

            return summary

        except wikipedia.DisambiguationError as e:
            return f"There are multiple results. Try '{e.options[0]}'."

        except wikipedia.PageError:
            return "I couldn't find anything on Wikipedia."

        except Exception as e:
            print(e)
            return "Something went wrong while searching Wikipedia."