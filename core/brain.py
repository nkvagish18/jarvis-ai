from core.router import Router
from core.ai import AI
from core.intent import Intent
from memory.extractor import MemoryExtractor
from memory.profile import Profile
from memory.search import MemorySearch
from memory.conversation import ConversationMemory
from core.plugin_router import PluginRouter
from utils.logger import logger
from typing import Optional


class Brain:

    def __init__(self) -> None:

        self.router = Router()

        self.ai = AI()

        self.extractor = MemoryExtractor()

        self.search = MemorySearch()

        self.conversation = ConversationMemory()

        self.plugin_router = PluginRouter()

    def process(self, command: str) -> Optional[str]:

        # ---------------- Intent ----------------

        intent = Intent.detect(command)

        # ---------------- Shutdown ----------------

        if intent == "shutdown":
            return "shutdown"

        # ---------------- Router ----------------

        plugin_response = self.plugin_router.execute(command)

        if plugin_response:
            return plugin_response


        if intent != "gemini":

            response = self.router.route(command)

            if response:
                return response

        # ====================================================
        # Everything below is ONLY for AI conversations
        # ====================================================

        # Save user message

        self.conversation.add_user(command)

        # Search Memory

        memory = self.search.search(command)

        if memory:

            self.conversation.add_assistant(memory)

            return memory

        # Build Context

        history = self.conversation.get_context()

        # Ask Gemini

        response = self.ai.chat(
            command,
            history
        )

        # Save assistant response

        self.conversation.add_assistant(response)

        # Extract facts

        facts = self.extractor.extract(command)

        if facts:

            Profile.remember(facts)

            logger.info("[Memory Updated]")

        return response