import os
from urllib import response
import requests
from dotenv import load_dotenv
from utils.config import Config
from core.parser import Parser
from utils.logger import logger

load_dotenv()

class NewsService:

    @staticmethod
    def get_news(command):

        category = Parser.extract_news_category(command)

        api_key = Config.NEWS_API_KEY

        url = (
            "https://newsapi.org/v2/everything"
            f"?q={category}"
            f"&sortBy=publishedAt"
            f"&language=en"
            f"&pageSize=3"
            f"&apiKey={api_key}"
        )

        try:
            
            response = requests.get(url, timeout=10)
            data = response.json()

            if response.status_code != 200:
                return "Unable to fetch the latest news."

            articles = data.get("articles", [])

            if not articles:
                return "No news articles were found."

            headlines = []

            for article in articles[:3]:
                headlines.append(article["title"])

            return headlines

        except Exception as e:
            logger.error("News",e)
            
            return (
                "I'm unable to fetch the latest news at the moment. "
                "Please try again later."
            )