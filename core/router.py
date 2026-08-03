from core.command_registry import CommandRegistry

from commands.apps import Apps
from commands.web import Web
from commands.system import System

from services.search import SearchService
from services.youtube import YouTubeService
from services.wikipedia import WikipediaService
from services.weather import WeatherService


class Router:

    def __init__(self):

        self.registry = CommandRegistry()

        self._register_apps()
        self._register_system()
        self._register_web()

    # -----------------------
    # Apps
    # -----------------------

    def _register_apps(self):

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

    # -----------------------
    # System
    # -----------------------

    def _register_system(self):

        self.registry.register(
            ["what time", "time"],
            lambda cmd: System.get_time()
        )

        self.registry.register(
            ["what date", "date"],
            lambda cmd: System.get_date()
        )

    # -----------------------
    # Web
    # -----------------------

    def _register_web(self):

        self.registry.register(
            [
                "weather",
                "temperature",
                "forecast",
                "humidity",
                "wind"
            ],
            lambda cmd: WeatherService.get_weather(cmd)
        )

        self.registry.register(
            ["open google"],
            lambda cmd: Web.open_google()
        )

        self.registry.register(
            ["open youtube"],
            lambda cmd: Web.open_youtube()
        )

        self.registry.register(
            ["play", "search youtube", "youtube"],
            lambda cmd: YouTubeService.search(cmd)
        )

        self.registry.register(
            ["search", "google"],
            lambda cmd: SearchService.google(cmd)
        )

        # Wikipedia only for encyclopedia topics
        self.registry.register(
            [
                "who is",
                "tell me about",
                "history of",
                "biography of",
                "capital of"
            ],
            lambda cmd: WikipediaService.search(cmd)
        )

    # -----------------------
    # Route
    # -----------------------

    def route(self, command):

        command = command.strip().lower()

        if command in [
            "shutdown",
            "exit",
            "quit",
            "goodbye"
        ]:
            return "shutdown"

        return self.registry.execute(command)