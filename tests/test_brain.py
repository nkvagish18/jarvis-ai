import unittest
from unittest.mock import MagicMock, patch

from core.brain import Brain


class TestBrain(unittest.TestCase):

    @patch("core.brain.PluginRouter")
    @patch("core.brain.ConversationMemory")
    @patch("core.brain.MemorySearch")
    @patch("core.brain.MemoryExtractor")
    @patch("core.brain.Profile")
    @patch("core.brain.AI")
    @patch("core.brain.Router")
    def test_gemini_intent(
        self,
        mock_router,
        mock_ai,
        mock_profile,
        mock_extractor,
        mock_search,
        mock_conversation,
        mock_plugin
    ):

        mock_plugin.return_value.execute.return_value = None
        mock_search.return_value.search.return_value = None

        mock_ai.return_value.chat.return_value = (
            "Recursion is a function calling itself."
        )

        mock_conversation.return_value.get_context.return_value = (
            "Previous conversation"
        )

        mock_extractor.return_value.extract.return_value = {}

        brain = Brain()

        result = brain.process(
            "What is recursion?"
        )

        mock_ai.return_value.chat.assert_called_once()

        mock_router.return_value.route.assert_not_called()

        self.assertEqual(
            result,
            "Recursion is a function calling itself."
        )

    @patch("core.brain.PluginRouter")
    @patch("core.brain.ConversationMemory")
    @patch("core.brain.MemorySearch")
    @patch("core.brain.MemoryExtractor")
    @patch("core.brain.Profile")
    @patch("core.brain.AI")
    @patch("core.brain.Router")
    def test_router_intent(
        self,
        mock_router,
        mock_ai,
        mock_profile,
        mock_extractor,
        mock_search,
        mock_conversation,
        mock_plugin
    ):

        mock_plugin.return_value.execute.return_value = None

        mock_router.return_value.route.return_value = (
            "Opening YouTube"
        )

        brain = Brain()

        result = brain.process(
            "open youtube"
        )

        mock_router.return_value.route.assert_called_once_with(
            "open youtube"
        )

        mock_ai.return_value.chat.assert_not_called()

        self.assertEqual(
            result,
            "Opening YouTube"
        )

    @patch("core.brain.PluginRouter")
    @patch("core.brain.ConversationMemory")
    @patch("core.brain.MemorySearch")
    @patch("core.brain.MemoryExtractor")
    @patch("core.brain.Profile")
    @patch("core.brain.AI")
    @patch("core.brain.Router")
    def test_weather_intent(
        self,
        mock_router,
        mock_ai,
        mock_profile,
        mock_extractor,
        mock_search,
        mock_conversation,
        mock_plugin
    ):

        mock_plugin.return_value.execute.return_value = None

        mock_router.return_value.route.return_value = (
            "Weather in Bangalore is 25 degrees."
        )

        brain = Brain()

        result = brain.process(
            "weather in Bangalore"
        )

        mock_router.return_value.route.assert_called_once_with(
            "weather in Bangalore"
        )

        mock_ai.return_value.chat.assert_not_called()

        self.assertEqual(
            result,
            "Weather in Bangalore is 25 degrees."
        )

    @patch("core.brain.PluginRouter")
    @patch("core.brain.ConversationMemory")
    @patch("core.brain.MemorySearch")
    @patch("core.brain.MemoryExtractor")
    @patch("core.brain.Profile")
    @patch("core.brain.AI")
    @patch("core.brain.Router")
    def test_plugin_command(
        self,
        mock_router,
        mock_ai,
        mock_profile,
        mock_extractor,
        mock_search,
        mock_conversation,
        mock_plugin
    ):

        mock_plugin.return_value.execute.return_value = (
            "Plugin executed successfully."
        )

        brain = Brain()

        result = brain.process(
            "run my plugin"
        )

        self.assertEqual(
            result,
            "Plugin executed successfully."
        )

        mock_router.return_value.route.assert_not_called()

        mock_ai.return_value.chat.assert_not_called()

    @patch("core.brain.PluginRouter")
    @patch("core.brain.ConversationMemory")
    @patch("core.brain.MemorySearch")
    @patch("core.brain.MemoryExtractor")
    @patch("core.brain.Profile")
    @patch("core.brain.AI")
    @patch("core.brain.Router")
    def test_memory_response(
        self,
        mock_router,
        mock_ai,
        mock_profile,
        mock_extractor,
        mock_search,
        mock_conversation,
        mock_plugin
    ):

        mock_plugin.return_value.execute.return_value = None

        mock_search.return_value.search.return_value = (
            "Your college is RNSIT."
        )

        brain = Brain()

        result = brain.process(
            "where do I study?"
        )

        self.assertEqual(
            result,
            "Your college is RNSIT."
        )

        mock_ai.return_value.chat.assert_not_called()

    @patch("core.brain.PluginRouter")
    @patch("core.brain.ConversationMemory")
    @patch("core.brain.MemorySearch")
    @patch("core.brain.MemoryExtractor")
    @patch("core.brain.Profile")
    @patch("core.brain.AI")
    @patch("core.brain.Router")
    def test_shutdown(
        self,
        mock_router,
        mock_ai,
        mock_profile,
        mock_extractor,
        mock_search,
        mock_conversation,
        mock_plugin
    ):

        brain = Brain()

        result = brain.process(
            "shutdown"
        )

        self.assertEqual(
            result,
            "shutdown"
        )

        mock_plugin.return_value.execute.assert_not_called()
        mock_router.return_value.route.assert_not_called()
        mock_ai.return_value.chat.assert_not_called()


if __name__ == "__main__":
    unittest.main()