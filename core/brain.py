from core.router import Router
from core.ai import AI
from core.intent import Intent


class Brain:

    def __init__(self):
        self.router = Router()
        self.ai = AI()

    def process(self, command):

        intent = Intent.detect(command)

        if intent == "gemini":
            return self.ai.ask(command)

        return self.router.route(command)