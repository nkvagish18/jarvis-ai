import unittest
from unittest.mock import patch, MagicMock

from services.news import NewsService


class TestNewsService(unittest.TestCase):

    @patch("services.news.Config.NEWS_API_KEY", "test_api_key")
    @patch("services.news.Parser.extract_news_category")
    @patch("services.news.requests.get")
    def test_news_success(self, mock_get, mock_category):

        mock_category.return_value = "technology"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "articles": [
                {"title": "Python 4 Released"},
                {"title": "New AI Model Announced"},
                {"title": "Technology Trends in 2026"}
            ]
        }

        mock_get.return_value = mock_response

        result = NewsService.get_news(
            "latest technology news"
        )

        self.assertEqual(
            result,
            [
                "Python 4 Released",
                "New AI Model Announced",
                "Technology Trends in 2026"
            ]
        )

        mock_category.assert_called_once_with(
            "latest technology news"
        )

        mock_get.assert_called_once_with(
            "https://newsapi.org/v2/everything"
            "?q=technology"
            "&sortBy=publishedAt"
            "&language=en"
            "&pageSize=3"
            "&apiKey=test_api_key",
            timeout=10
        )


    @patch("services.news.Config.NEWS_API_KEY", "test_api_key")
    @patch("services.news.Parser.extract_news_category")
    @patch("services.news.requests.get")
    def test_news_limits_to_three_articles(
        self,
        mock_get,
        mock_category
    ):

        mock_category.return_value = "AI"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "articles": [
                {"title": "Article 1"},
                {"title": "Article 2"},
                {"title": "Article 3"},
                {"title": "Article 4"},
                {"title": "Article 5"}
            ]
        }

        mock_get.return_value = mock_response

        result = NewsService.get_news(
            "AI news"
        )

        self.assertEqual(
            result,
            [
                "Article 1",
                "Article 2",
                "Article 3"
            ]
        )

        self.assertEqual(
            len(result),
            3
        )


    @patch("services.news.Config.NEWS_API_KEY", "test_api_key")
    @patch("services.news.Parser.extract_news_category")
    @patch("services.news.requests.get")
    def test_news_api_error(
        self,
        mock_get,
        mock_category
    ):

        mock_category.return_value = "sports"

        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.json.return_value = {}

        mock_get.return_value = mock_response

        result = NewsService.get_news(
            "latest sports news"
        )

        self.assertEqual(
            result,
            "Unable to fetch the latest news."
        )


    @patch("services.news.Config.NEWS_API_KEY", "test_api_key")
    @patch("services.news.Parser.extract_news_category")
    @patch("services.news.requests.get")
    def test_no_articles(
        self,
        mock_get,
        mock_category
    ):

        mock_category.return_value = "science"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "articles": []
        }

        mock_get.return_value = mock_response

        result = NewsService.get_news(
            "science news"
        )

        self.assertEqual(
            result,
            "No news articles were found."
        )


    @patch("services.news.Config.NEWS_API_KEY", "test_api_key")
    @patch("services.news.Parser.extract_news_category")
    @patch("services.news.requests.get")
    def test_request_failure(
        self,
        mock_get,
        mock_category
    ):

        mock_category.return_value = "world"

        mock_get.side_effect = Exception(
            "Network connection failed"
        )

        result = NewsService.get_news(
            "world news"
        )

        self.assertEqual(
            result,
            "I'm unable to fetch the latest news at the moment. "
            "Please try again later."
        )


if __name__ == "__main__":
    unittest.main()