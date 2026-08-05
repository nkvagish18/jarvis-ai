import json
from core.ai import AI


class MemoryExtractor:

    def __init__(self):
        self.ai = AI()

    def extract(self, message):

        prompt = f"""
You are an AI memory extractor.

Your task is to extract ONLY long-term personal facts.

Examples of things to remember:
- Name
- Age
- City
- College
- Job
- Skills
- Programming languages
- Goals
- Birthday
- Interests
- Preferences
- Devices
- Pets

DO NOT remember:
- Questions
- Temporary requests
- Greetings
- Conversations
- Opinions that are not personal facts

Return ONLY valid JSON.

If nothing should be remembered, return:

{{}}

User:

{message}
"""

        return self.ai.extract_json(prompt)