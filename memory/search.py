import json

from core.ai import AI
from memory.manager import MemoryManager


class MemorySearch:

    def __init__(self):
        self.ai = AI()

    def search(self, question):

        memory = MemoryManager.get_all()

        if not memory:
            return None

        prompt = f"""
You are Jarvis.

Below is the user's long-term memory.

{json.dumps(memory, indent=2)}

Answer ONLY using the information in memory.

If the answer is not present, reply exactly:

UNKNOWN

Question:

{question}
"""

        answer = self.ai.ask(prompt).strip()

        if answer.upper() == "UNKNOWN":
            return None

        return answer