import unittest
from unittest.mock import patch

from memory.search import MemorySearch


class TestMemorySearch(unittest.TestCase):

    @patch("memory.search.AI")
    @patch("memory.search.MemoryManager.get_all")
    def test_memory_answer(
        self,
        mock_get_all,
        mock_ai
    ):

        mock_get_all.return_value = {
            "name": "Vagish",
            "skills": ["Python", "AI"]
        }

        mock_ai.return_value.ask.return_value = (
            "Your name is Vagish."
        )

        search = MemorySearch()

        result = search.search(
            "What is my name?"
        )

        self.assertEqual(
            result,
            "Your name is Vagish."
        )

        mock_get_all.assert_called_once()
        mock_ai.return_value.ask.assert_called_once()

    @patch("memory.search.AI")
    @patch("memory.search.MemoryManager.get_all")
    def test_unknown_memory(
        self,
        mock_get_all,
        mock_ai
    ):

        mock_get_all.return_value = {
            "name": "Vagish"
        }

        mock_ai.return_value.ask.return_value = "UNKNOWN"

        search = MemorySearch()

        result = search.search(
            "What is my favorite food?"
        )

        self.assertIsNone(result)

    @patch("memory.search.AI")
    @patch("memory.search.MemoryManager.get_all")
    def test_empty_memory(
        self,
        mock_get_all,
        mock_ai
    ):

        mock_get_all.return_value = {}

        search = MemorySearch()

        result = search.search(
            "What is my name?"
        )

        self.assertIsNone(result)

        mock_ai.return_value.ask.assert_not_called()

    @patch("memory.search.AI")
    @patch("memory.search.MemoryManager.get_all")
    def test_unknown_case_insensitive(
        self,
        mock_get_all,
        mock_ai
    ):

        mock_get_all.return_value = {
            "name": "Vagish"
        }

        mock_ai.return_value.ask.return_value = "unknown"

        search = MemorySearch()

        result = search.search(
            "What is my age?"
        )

        self.assertIsNone(result)

    @patch("memory.search.AI")
    @patch("memory.search.MemoryManager.get_all")
    def test_question_is_sent_to_ai(
        self,
        mock_get_all,
        mock_ai
    ):

        mock_get_all.return_value = {
            "name": "Vagish"
        }

        mock_ai.return_value.ask.return_value = (
            "Your name is Vagish."
        )

        search = MemorySearch()

        search.search("What is my name?")

        mock_ai.return_value.ask.assert_called_once()

        prompt = (
            mock_ai.return_value
            .ask
            .call_args[0][0]
        )

        self.assertIn(
            "What is my name?",
            prompt
        )

        self.assertIn(
            "Vagish",
            prompt
        )


if __name__ == "__main__":
    unittest.main()