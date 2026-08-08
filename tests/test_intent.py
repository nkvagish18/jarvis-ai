import unittest

from core.intent import Intent

class TestIntent(unittest.TestCase):

    def test_weather(self):
        self.assertEqual(
            Intent.detect("weather in Bangalore"),
            "weather"
        )

    def test_youtube(self):
        self.assertEqual(
            Intent.detect("play music on youtube"),
            "youtube"
        )

    def test_google(self):
        self.assertEqual(
            Intent.detect("search latest AI news"),
            "google"
        )

    def test_shutdown(self):
        self.assertEqual(
            Intent.detect("goodbye"),
            "shutdown"
        )

    def test_gemini(self):
        self.assertEqual(
            Intent.detect("explain recursion"),
            "gemini"
        )


if __name__ == "__main__":
    unittest.main()