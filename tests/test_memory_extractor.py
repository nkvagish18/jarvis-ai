import unittest
from unittest.mock import patch

from memory.extractor import MemoryExtractor


class TestMemoryExtractor(unittest.TestCase):

    @patch("memory.extractor.AI")
    def test_extract_facts(self, mock_ai):

        mock_ai.return_value.extract_json.return_value = {
            "name": "Vagish",
            "skills": ["Python"]
        }

        extractor = MemoryExtractor()

        result = extractor.extract(
            "My name is Vagish and I know Python."
        )

        self.assertEqual(
            result,
            {
                "name": "Vagish",
                "skills": ["Python"]
            }
        )

        mock_ai.return_value.extract_json.assert_called_once()

    @patch("memory.extractor.AI")
    def test_no_facts(self, mock_ai):

        mock_ai.return_value.extract_json.return_value = {}

        extractor = MemoryExtractor()

        result = extractor.extract(
            "What is the weather today?"
        )

        self.assertEqual(
            result,
            {}
        )

    @patch("memory.extractor.AI")
    def test_extract_multiple_facts(self, mock_ai):

        mock_ai.return_value.extract_json.return_value = {
            "name": "Vagish",
            "education": {
                "city": "Bangalore",
                "institution": "RNSIT"
            },
            "skills": [
                "Python",
                "AI"
            ]
        }

        extractor = MemoryExtractor()

        result = extractor.extract(
            "I'm Vagish, studying at RNSIT in Bangalore. "
            "I know Python and AI."
        )

        self.assertEqual(
            result["name"],
            "Vagish"
        )

        self.assertEqual(
            result["education"]["city"],
            "Bangalore"
        )

        self.assertEqual(
            result["education"]["institution"],
            "RNSIT"
        )

        self.assertEqual(
            result["skills"],
            ["Python", "AI"]
        )

    @patch("memory.extractor.AI")
    def test_ai_extract_json_is_called_with_prompt(
        self,
        mock_ai
    ):

        mock_ai.return_value.extract_json.return_value = {}

        extractor = MemoryExtractor()

        extractor.extract("Hello Jarvis")

        mock_ai.return_value.extract_json.assert_called_once()

        prompt = (
            mock_ai.return_value
            .extract_json
            .call_args[0][0]
        )

        self.assertIn(
            "AI memory extractor",
            prompt
        )

        self.assertIn(
            "Hello Jarvis",
            prompt
        )


if __name__ == "__main__":
    unittest.main()