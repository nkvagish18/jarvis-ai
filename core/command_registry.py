class CommandRegistry:

    def __init__(self):
        self.commands = []

    def register(self, keywords, action):
        self.commands.append((keywords, action))

    def execute(self, command):

        command = command.lower().strip()

        for keywords, action in self.commands:

            if any(keyword in command for keyword in keywords):
                return action(command)

        return None