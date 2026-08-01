from core.command_registry import CommandRegistry
from commands.apps import Apps
from commands.web import Web
from commands.system import System
from services.search import SearchService
from services.youtube import YouTubeService
from services.wikipedia import WikipediaService


class Router:

    def __init__(self):

        self.registry = CommandRegistry()

        # Apps
        self.registry.register(
            ["open notepad"],
            lambda cmd: Apps.open_notepad()
        )

        self.registry.register(
            ["open calculator"],
            lambda cmd: Apps.open_calculator()
        )

        self.registry.register(
            ["open paint"],
            lambda cmd: Apps.open_paint()
        )

        self.registry.register(
            ["open cmd", "open command prompt"],
            lambda cmd: Apps.open_cmd()
        )

        self.registry.register(
            ["open file explorer"],
            lambda cmd: Apps.open_explorer()
        )

        # Web
        self.registry.register(
            ["open google"],
            lambda cmd: Web.open_google()
        )

        self.registry.register(
            ["search","google"],
            lambda cmd: SearchService.google(cmd)
        )

        self.registry.register(
            ["who is", "what is", "tell me about", "explain"],
            lambda cmd: WikipediaService.search(cmd)
        )

        self.registry.register(
            ["open youtube"],
            lambda cmd: Web.open_youtube()
        )

        self.registry.register(
            ["play","search youtube","youtube"],
            lambda cmd: YouTubeService.search(cmd)
        )

        # System
        self.registry.register(
            ["what time", "time"],
            lambda cmd: System.get_time()
        )

        self.registry.register(
            ["what date", "date"],
            lambda cmd: System.get_date()
        )

    def route(self, command):

        result = self.registry.execute(command)

        if result:
            return result

        if "shutdown" in command.lower():
            return "shutdown"

        return None