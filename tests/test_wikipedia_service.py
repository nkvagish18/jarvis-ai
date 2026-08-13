import unittest
from unittest.mock import patch, MagicMock

from services.wikipedia import WikipediaService


class TestWikipediaService(unittest.TestCase):

    @patch("services.wikipedia.Parser.extract_wikipedia_query")
    @patch("services.wikipedia.requests.get")
    def test_wikipedia_success(
        self,
        mock_get,
        mock_query
    ):

        mock_query.return_value = "Virat Kohli"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "extract": "Virat Kohli is an Indian international cricketer."
        }

        mock_get.return_value = mock_response

        result = WikipediaService.search(
            "tell me about Virat Kohli"
        )

        self.assertEqual(
            result,
            "Virat Kohli is an Indian international cricketer."
        )

        mock_query.assert_called_once_with(
            "tell me about Virat Kohli"
        )

        mock_get.assert_called_once_with(
            "https://en.wikipedia.org/api/rest_v1/page/summary/"
            "Virat_Kohli",
            headers={
                "User-Agent": "JarvisAI/1.0"
            },
            timeout=10
        )


    @patch("services.wikipedia.Parser.extract_wikipedia_query")
    @patch("services.wikipedia.requests.get")
    def test_wikipedia_query_with_spaces(
        self,
        mock_get,
        mock_query
    ):

        mock_query.return_value = "Albert Einstein"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "extract": "Albert Einstein was a German-born physicist."
        }

        mock_get.return_value = mock_response

        result = WikipediaService.search(
            "who is Albert Einstein"
        )

        self.assertEqual(
            result,
            "Albert Einstein was a German-born physicist."
        )

        mock_get.assert_called_once_with(
            "https://en.wikipedia.org/api/rest_v1/page/summary/"
            "Albert_Einstein",
            headers={
                "User-Agent": "JarvisAI/1.0"
            },
            timeout=10
        )


    @patch("services.wikipedia.Parser.extract_wikipedia_query")
    @patch("services.wikipedia.requests.get")
    def test_wikipedia_page_not_found(
        self,
        mock_get,
        mock_query
    ):

        mock_query.return_value = "Unknown Person"

        mock_response = MagicMock()
        mock_response.status_code = 404

        mock_get.return_value = mock_response

        result = WikipediaService.search(
            "tell me about Unknown Person"
        )

        self.assertEqual(
            result,
            "I couldn't find anything on Wikipedia."
        )


    @patch("services.wikipedia.Parser.extract_wikipedia_query")
    @patch("services.wikipedia.requests.get")
    def test_wikipedia_missing_extract(
        self,
        mock_get,
        mock_query
    ):

        mock_query.return_value = "Python"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "title": "Python"
        }

        mock_get.return_value = mock_response

        result = WikipediaService.search(
            "tell me about Python"
        )

        self.assertEqual(
            result,
            "I couldn't find anything on Wikipedia."
        )


    @patch("services.wikipedia.Parser.extract_wikipedia_query")
    @patch("services.wikipedia.requests.get")
    def test_wikipedia_request_failure(
        self,
        mock_get,
        mock_query
    ):

        mock_query.return_value = "Python"

        mock_get.side_effect = Exception(
            "Network connection failed"
        )

        result = WikipediaService.search(
            "tell me about Python"
        )

        self.assertEqual(
            result,
            "I couldn't find information about that topic."
        )


if __name__ == "__main__":
    unittest.main()