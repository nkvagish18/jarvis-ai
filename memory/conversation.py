from collections import deque
from utils.config import Config

class ConversationMemory:
    """
    Stores recent conversation history.
    """

    def __init__(self,max_messages=Config.MAX_CONVERSATION_HISTORY):
        self.history = deque(maxlen=max_messages)

    def add_user(self, message):
        self.history.append({
            "role": "user",
            "content": message
        })

    def add_assistant(self, message):
        self.history.append({
            "role": "assistant",
            "content": message
        })

    def get_context(self):

        if not self.history:
            return ""

        context = []

        for msg in self.history:

            role = msg["role"].capitalize()

            context.append(
                f"{role}: {msg['content']}"
            )

        return "\n".join(context)

    def clear(self):
        self.history.clear()