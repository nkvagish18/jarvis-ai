from core.router import Router
from core.ai import AI
from core.intent import Intent

from memory.extractor import MemoryExtractor
from memory.profile import Profile
from memory.search import MemorySearch


class Brain:

    def __init__(self):

        self.router = Router()
        self.ai = AI()

        self.extractor = MemoryExtractor()
        self.search = MemorySearch()

    def process(self, command):

        # ---------------- AUTO MEMORY ----------------

        facts = self.extractor.extract(command)

        if facts:

            Profile.remember(facts)

            print("[Memory Updated]")
            print(facts)

        # ---------------- MEMORY SEARCH ----------------

        memory_answer = self.search.search(command)

        if memory_answer:

            return memory_answer

        # ---------------- INTENT ----------------

        intent = Intent.detect(command)

        if intent == "gemini":

            return self.ai.ask(command)

        # ---------------- ROUTER ----------------

        response = self.router.route(command)

        if response:

            return response

        # ---------------- FALLBACK ----------------

        return self.ai.ask(command)