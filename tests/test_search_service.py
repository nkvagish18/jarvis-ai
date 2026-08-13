import unittest
from unittest.mock import patch

from services.search import SearchService


class TestSearchService(unittest.TestCase):

    @patch("services.search.Parser.extract_google_query")
    @patch("services.search.webbrowser.open")
    def test_google_success(self, mock_open, mock_query):

        mock_query.return_value = "Python tutorials"

        result = SearchService.google(
            "search Python tutorials"
        )

        self.assertEqual(
            result,
            "Searching Google for Python tutorials"
        )

        mock_open.assert_called_once_with(
            "https://www.google.com/search?q=Python tutorials"
        )

    @patch("services.search.Parser.extract_google_query")
    @patch("services.search.webbrowser.open")
    def test_google_query_extraction(self, mock_open, mock_query):

        mock_query.return_value = "machine learning"

        SearchService.google(
            "search machine learning"
        )

        mock_query.assert_called_once_with(
            "search machine learning"
        )

    @patch("services.search.Parser.extract_google_query")
    @patch("services.search.webbrowser.open")
    def test_google_browser_error(self, mock_open, mock_query):

        mock_query.return_value = "Python"

        mock_open.side_effect = Exception(
            "Browser failed"
        )

        result = SearchService.google(
            "search Python"
        )

        self.assertEqual(
            result,
            "I couldn't perform the Google search right now."
        )

    @patch("services.search.Parser.extract_google_query")
    @patch("services.search.webbrowser.open")
    def test_google_empty_query(self, mock_open, mock_query):

        mock_query.return_value = ""

        result = SearchService.google(
            "search"
        )

        self.assertEqual(
            result,
            "Searching Google for "
        )

        mock_open.assert_called_once_with(
            "https://www.google.com/search?q="
        )


if __name__ == "__main__":
    unittest.main()