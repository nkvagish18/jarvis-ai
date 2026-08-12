import unittest
from unittest.mock import patch

from core.intent import Intent
from core.brain import Brain


class TestJarvisIntegration(unittest.TestCase):

    # ---------------- Shutdown ----------------

    def test_shutdown_flow(self):

        command = "shutdown"

        intent = Intent.detect(command)

        self.assertEqual(
            intent,
            "shutdown"
        )

        brain = Brain()

        response = brain.process(command)

        self.assertEqual(
            response,
            "shutdown"
        )

    # ---------------- System ----------------

    @patch("commands.system.datetime")
    def test_system_time_flow(self, mock_datetime):

        mock_datetime.now.return_value.strftime.return_value = (
            "The time is 10:30 AM"
        )

        command = "what is the time"

        intent = Intent.detect(command)

        self.assertEqual(
            intent,
            "system"
        )

        brain = Brain()

        response = brain.process(command)

        self.assertEqual(
            response,
            "The time is 10:30 AM"
        )

    # ---------------- Weather ----------------

    @patch("services.weather.WeatherService.get_weather")
    def test_weather_flow(self, mock_weather):

        mock_weather.return_value = (
            "The weather in Bangalore is 25°C."
        )

        command = "weather in Bangalore"

        intent = Intent.detect(command)

        self.assertEqual(
            intent,
            "weather"
        )

        brain = Brain()

        response = brain.process(command)

        mock_weather.assert_called_once_with(
            "weather in bangalore"
        )

        self.assertEqual(
            response,
            "The weather in Bangalore is 25°C."
        )

        # ---------------- News ----------------

    @patch("services.news.NewsService.get_news")
    def test_news_flow(self, mock_news):

        mock_news.return_value = (
            "Here are today's top headlines. "
            "Headline one. Headline two. Headline three."
        )

        command = "latest news"

        intent = Intent.detect(command)

        self.assertEqual(
            intent,
            "google"
        )

        brain = Brain()

        response = brain.process(command)

        mock_news.assert_called_once_with(
            "latest news"
        )

        self.assertEqual(
            response,
            "Here are today's top headlines. "
            "Headline one. Headline two. Headline three."
        )

    # ---------------- YouTube ----------------

    @patch("services.youtube.YouTubeService.search")
    def test_youtube_flow(self, mock_youtube):

        mock_youtube.return_value = (
            "Searching YouTube for music"
        )

        command = "search youtube for music"

        intent = Intent.detect(command)

        self.assertEqual(
            intent,
            "youtube"
        )

        brain = Brain()

        response = brain.process(command)

        mock_youtube.assert_called_once_with(
            "search youtube for music"
        )

        self.assertEqual(
            response,
            "Searching YouTube for music"
        )

    # ---------------- Gemini ----------------

    @patch("core.brain.MemorySearch")
    @patch("core.brain.AI")
    def test_gemini_flow(self, mock_ai, mock_search):

        # Make sure Brain does NOT answer from memory
        mock_search.return_value.search.return_value = None

        # Mock Gemini response
        mock_ai.return_value.chat.return_value = (
            "Recursion is a programming technique where "
            "a function calls itself."
        )

        command = "what is recursion"

        intent = Intent.detect(command)

        self.assertEqual(
            intent,
            "gemini"
        )

        brain = Brain()

        response = brain.process(command)

        mock_search.return_value.search.assert_called_once_with(
            command
        )

        mock_ai.return_value.chat.assert_called_once()

        self.assertEqual(
            response,
            "Recursion is a programming technique where "
            "a function calls itself."
        )

    # ---------------- Memory ----------------

    @patch("core.brain.MemorySearch")
    @patch("core.brain.AI")
    def test_memory_first_flow(self, mock_ai, mock_search):

        mock_search.return_value.search.return_value = (
            "You study at RNSIT in Bangalore."
        )

        brain = Brain()

        command = "where do I study"

        response = brain.process(command)

        mock_search.return_value.search.assert_called_once_with(
            command
        )

        # Gemini must NOT be called
        mock_ai.return_value.chat.assert_not_called()

        self.assertEqual(
            response,
            "You study at RNSIT in Bangalore."
        )

        # ---------------- Memory Learning ----------------

    @patch("core.brain.Profile")
    @patch("core.brain.MemoryExtractor")
    @patch("core.brain.MemorySearch")
    @patch("core.brain.AI")
    def test_memory_learning_flow(
        self,
        mock_ai,
        mock_search,
        mock_extractor,
        mock_profile
    ):

        # No existing memory
        mock_search.return_value.search.return_value = None

        # Mock Gemini response
        mock_ai.return_value.chat.return_value = (
            "Got it! I'll remember that."
        )

        # Mock extracted fact
        mock_extractor.return_value.extract.return_value = {
            "skills": ["Python"]
        }

        brain = Brain()

        command = "I am learning Python"

        response = brain.process(command)

        # Gemini was used
        mock_ai.return_value.chat.assert_called_once()

        # Memory extraction happened
        mock_extractor.return_value.extract.assert_called_once_with(
            command
        )

        # Profile was updated
        mock_profile.remember.assert_called_once_with(
            {
                "skills": ["Python"]
            }
        )

        self.assertEqual(
            response,
            "Got it! I'll remember that."
        )


if __name__ == "__main__":
    unittest.main()