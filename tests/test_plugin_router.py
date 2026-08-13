import unittest
from unittest.mock import patch, MagicMock

from core.plugin_router import PluginRouter


class TestPluginRouter(unittest.TestCase):

    @patch("core.plugin_router.PluginLoader.load")
    def test_matching_plugin(self, mock_load):

        class TestPlugin:
            keywords = ["hello"]

            @staticmethod
            def execute(command):
                return "Hello from plugin!"

        mock_module = MagicMock()
        mock_module.TestPlugin = TestPlugin

        mock_load.return_value = [mock_module]

        router = PluginRouter()

        result = router.execute("hello jarvis")

        self.assertEqual(
            result,
            "Hello from plugin!"
        )

    @patch("core.plugin_router.PluginLoader.load")
    def test_unknown_command(self, mock_load):

        class TestPlugin:
            keywords = ["hello"]

            @staticmethod
            def execute(command):
                return "Hello!"

        mock_module = MagicMock()
        mock_module.TestPlugin = TestPlugin

        mock_load.return_value = [mock_module]

        router = PluginRouter()

        result = router.execute("open calculator")

        self.assertIsNone(result)

    @patch("core.plugin_router.PluginLoader.load")
    def test_case_insensitive_matching(self, mock_load):

        class TestPlugin:
            keywords = ["hello"]

            @staticmethod
            def execute(command):
                return "Hello!"

        mock_module = MagicMock()
        mock_module.TestPlugin = TestPlugin

        mock_load.return_value = [mock_module]

        router = PluginRouter()

        result = router.execute("HELLO JARVIS")

        self.assertEqual(
            result,
            "Hello!"
        )

    @patch("core.plugin_router.PluginLoader.load")
    def test_plugin_receives_lowercase_command(self, mock_load):

        class TestPlugin:

            keywords = ["youtube"]

            execute = MagicMock(
                return_value="YouTube opened"
            )

        mock_module = MagicMock()
        mock_module.TestPlugin = TestPlugin

        mock_load.return_value = [mock_module]

        router = PluginRouter()

        router.execute("Open YouTube")

        TestPlugin.execute.assert_called_once_with(
            "open youtube"
        )

    @patch("core.plugin_router.PluginLoader.load")
    def test_first_matching_plugin_is_executed(
        self,
        mock_load
    ):

        class PluginOne:

            keywords = ["hello"]

            execute = MagicMock(
                return_value="Plugin One"
            )

        class PluginTwo:

            keywords = ["hello"]

            execute = MagicMock(
                return_value="Plugin Two"
            )

        mock_module = MagicMock()

        mock_module.PluginOne = PluginOne
        mock_module.PluginTwo = PluginTwo

        mock_load.return_value = [mock_module]

        router = PluginRouter()

        result = router.execute("hello")

        self.assertEqual(
            result,
            "Plugin One"
        )

        PluginOne.execute.assert_called_once()

        PluginTwo.execute.assert_not_called()


if __name__ == "__main__":
    unittest.main()