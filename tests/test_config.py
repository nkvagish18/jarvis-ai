import unittest
import os
from unittest.mock import patch

from utils.config import Config


class TestConfig(unittest.TestCase):

    def test_gemini_model(self):
        self.assertEqual(
            Config.GEMINI_MODEL,
            "gemini-2.5-flash"
        )

    def test_conversation_history(self):
        self.assertEqual(
            Config.MAX_CONVERSATION_HISTORY,
            10
        )

    def test_memory_file(self):
        self.assertEqual(
            Config.MEMORY_FILE,
            "memory/storage.json"
        )

    @patch.dict(
        os.environ,
        {
            "GEMINI_API_KEY": "test-gemini-key",
            "WEATHER_API_KEY": "test-weather-key",
            "NEWS_API_KEY": "test-news-key"
        }
    )
    def test_environment_variables_exist(self):

        self.assertIsNotNone(
            os.getenv("GEMINI_API_KEY")
        )

        self.assertIsNotNone(
            os.getenv("WEATHER_API_KEY")
        )

        self.assertIsNotNone(
            os.getenv("NEWS_API_KEY")
        )


if __name__ == "__main__":
    unittest.main()