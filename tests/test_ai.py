import unittest
from unittest.mock import MagicMock, patch

from core.ai import AI


class TestAI(unittest.TestCase):

    @patch("core.ai.genai.Client")
    def test_ask_success(self, mock_client):

        mock_response = MagicMock()
        mock_response.text = "Recursion is a function calling itself."

        mock_client.return_value.models.generate_content.return_value = (
            mock_response
        )

        ai = AI()

        result = ai.ask("What is recursion?")

        self.assertEqual(
            result,
            "Recursion is a function calling itself."
        )

    @patch("core.ai.genai.Client")
    def test_ask_empty_response(self, mock_client):

        mock_response = MagicMock()
        mock_response.text = None

        mock_client.return_value.models.generate_content.return_value = (
            mock_response
        )

        ai = AI()

        result = ai.ask("Explain AI")

        self.assertEqual(
            result,
            "I couldn't generate a response."
        )

    @patch("core.ai.genai.Client")
    def test_ask_503_error(self, mock_client):

        mock_client.return_value.models.generate_content.side_effect = (
            Exception("503 UNAVAILABLE")
        )

        ai = AI()

        result = ai.ask("Explain AI")

        self.assertEqual(
            result,
            "I'm a little busy right now. Please try again in a few seconds."
        )

    @patch("core.ai.genai.Client")
    def test_ask_429_error(self, mock_client):

        mock_client.return_value.models.generate_content.side_effect = (
            Exception("429 RESOURCE EXHAUSTED")
        )

        ai = AI()

        result = ai.ask("Explain Python")

        self.assertEqual(
            result,
            "I've reached my request limit for now. Please try again later."
        )

    @patch("core.ai.genai.Client")
    def test_ask_401_error(self, mock_client):

        mock_client.return_value.models.generate_content.side_effect = (
            Exception("401 UNAUTHENTICATED")
        )

        ai = AI()

        result = ai.ask("Explain machine learning")

        self.assertEqual(
            result,
            "There seems to be an authentication problem with the AI service."
        )

    @patch("core.ai.genai.Client")
    def test_ask_general_error(self, mock_client):

        mock_client.return_value.models.generate_content.side_effect = (
            Exception("Network connection failed")
        )

        ai = AI()

        result = ai.ask("Hello")

        self.assertEqual(
            result,
            "I'm sorry, I couldn't process your request right now."
        )

    @patch("core.ai.genai.Client")
    def test_extract_json_success(self, mock_client):

        mock_response = MagicMock()

        mock_response.text = """
        {
            "name": "Vagish",
            "skills": ["Python", "AI"]
        }
        """

        mock_client.return_value.models.generate_content.return_value = (
            mock_response
        )

        ai = AI()

        result = ai.extract_json(
            "Extract user information as JSON."
        )

        self.assertEqual(
            result["name"],
            "Vagish"
        )

        self.assertEqual(
            result["skills"],
            ["Python", "AI"]
        )

    @patch("core.ai.genai.Client")
    def test_extract_json_markdown(self, mock_client):

        mock_response = MagicMock()

        mock_response.text = """
        ```json
        {
            "name": "Vagish"
        }
        ```
        """

        mock_client.return_value.models.generate_content.return_value = (
            mock_response
        )

        ai = AI()

        result = ai.extract_json(
            "Return the user's name as JSON."
        )

        self.assertEqual(
            result["name"],
            "Vagish"
        )

    @patch("core.ai.genai.Client")
    def test_extract_json_invalid(self, mock_client):

        mock_response = MagicMock()
        mock_response.text = "This is not valid JSON."

        mock_client.return_value.models.generate_content.return_value = (
            mock_response
        )

        ai = AI()

        result = ai.extract_json(
            "Return JSON."
        )

        self.assertEqual(
            result,
            {}
        )

    @patch("core.ai.genai.Client")
    def test_chat(self, mock_client):

        mock_response = MagicMock()
        mock_response.text = "Hello Vagish!"

        mock_client.return_value.models.generate_content.return_value = (
            mock_response
        )

        ai = AI()

        result = ai.chat(
            "Hello",
            "Previous conversation"
        )

        self.assertEqual(
            result,
            "Hello Vagish!"
        )


if __name__ == "__main__":
    unittest.main()