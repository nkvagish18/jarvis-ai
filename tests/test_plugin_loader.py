import unittest
from unittest.mock import patch, MagicMock

from core.plugin_loader import PluginLoader


class TestPluginLoader(unittest.TestCase):

    @patch("core.plugin_loader.importlib.import_module")
    @patch("core.plugin_loader.pkgutil.iter_modules")
    def test_load_plugins(
        self,
        mock_iter_modules,
        mock_import_module
    ):

        mock_iter_modules.return_value = [
            (None, "weather_plugin", False),
            (None, "youtube_plugin", False),
        ]

        weather_module = MagicMock()
        youtube_module = MagicMock()

        mock_import_module.side_effect = [
            weather_module,
            youtube_module
        ]

        result = PluginLoader.load()

        self.assertEqual(
            result,
            [
                weather_module,
                youtube_module
            ]
        )

        self.assertEqual(
            mock_import_module.call_count,
            2
        )

        mock_import_module.assert_any_call(
            "plugins.weather_plugin"
        )

        mock_import_module.assert_any_call(
            "plugins.youtube_plugin"
        )

    @patch("core.plugin_loader.pkgutil.iter_modules")
    def test_no_plugins(self, mock_iter_modules):

        mock_iter_modules.return_value = []

        result = PluginLoader.load()

        self.assertEqual(
            result,
            []
        )

    @patch("core.plugin_loader.importlib.import_module")
    @patch("core.plugin_loader.pkgutil.iter_modules")
    def test_plugins_are_loaded_in_discovery_order(
        self,
        mock_iter_modules,
        mock_import_module
    ):

        mock_iter_modules.return_value = [
            (None, "first_plugin", False),
            (None, "second_plugin", False),
            (None, "third_plugin", False),
        ]

        first = MagicMock()
        second = MagicMock()
        third = MagicMock()

        mock_import_module.side_effect = [
            first,
            second,
            third
        ]

        result = PluginLoader.load()

        self.assertEqual(
            result,
            [first, second, third]
        )


if __name__ == "__main__":
    unittest.main()