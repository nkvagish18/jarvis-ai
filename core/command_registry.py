import re
from typing import Callable


class CommandRegistry:

    def __init__(self) -> None:
        self.commands: list[tuple[list[str], Callable[[str], str]]] = []

    def register(
        self,
        keywords: list[str],
        action: Callable[[str], str]
    ) -> None:

        self.commands.append((keywords, action))

    def execute(self, command: str) -> str | None:

        command = command.lower().strip()

        for keywords, action in self.commands:

            for keyword in keywords:

                pattern = rf"\b{re.escape(keyword.lower())}\b"

                if re.search(pattern, command):
                    return action(command)

        return None