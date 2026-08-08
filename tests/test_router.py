import unittest
from unittest.mock import patch

from core.router import Router


class TestRouter(unittest.TestCase):

    def setUp(self):
        self.router = Router()

    @patch("core.router.SearchService.google")
    def test_google_search(self, mock_google):

        mock_google.return_value = "Google result"

        result = self.router.route(
            "search Python tutorials"
        )

        mock_google.assert_called_once_with(
            "search python tutorials"
        )

        self.assertEqual(
            result,
            "Google result"
        )

    @patch("core.router.WeatherService.get_weather")
    def test_weather(self, mock_weather):

        mock_weather.return_value = "Weather result"

        result = self.router.route(
            "weather in Bangalore"
        )

        mock_weather.assert_called_once_with(
            "weather in bangalore"
        )

        self.assertEqual(
            result,
            "Weather result"
        )

    @patch("core.router.YouTubeService.search")
    def test_youtube(self, mock_youtube):

        mock_youtube.return_value = "YouTube result"

        result = self.router.route(
            "play music"
        )

        mock_youtube.assert_called_once_with(
            "play music"
        )

        self.assertEqual(
            result,
            "YouTube result"
        )

    def test_unknown_command(self):

        result = self.router.route(
            "completely unknown command"
        )

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()