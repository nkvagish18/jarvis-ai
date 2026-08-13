import unittest
from unittest.mock import patch, MagicMock

from services.weather_service import WeatherService


class TestWeatherService(unittest.TestCase):

    @patch("services.weather_service.Config.WEATHER_API_KEY", "test_api_key")
    @patch("services.weather_service.Parser.extract_weather_city")
    @patch("services.weather_service.requests.get")
    def test_weather_success(self, mock_get, mock_city):

        mock_city.return_value = "Bangalore"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "weather": [
                {
                    "description": "clear sky"
                }
            ],
            "main": {
                "temp": 28,
                "feels_like": 29,
                "humidity": 60
            },
            "wind": {
                "speed": 3.5
            }
        }

        mock_get.return_value = mock_response

        result = WeatherService.get_weather(
            "weather in Bangalore"
        )

        self.assertEqual(
            result,
            "The weather in Bangalore is Clear Sky. "
            "The temperature is 28 degrees Celsius, "
            "feels like 29 degrees, "
            "humidity is 60 percent, "
            "and wind speed is 3.5 meters per second."
        )

        mock_get.assert_called_once_with(
            "https://api.openweathermap.org/data/2.5/weather"
            "?q=Bangalore"
            "&appid=test_api_key"
            "&units=metric",
            timeout=10
        )


    @patch("services.weather_service.Parser.extract_weather_city")
    @patch("services.weather_service.requests.get")
    def test_default_city(self, mock_get, mock_city):

        mock_city.return_value = None

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "weather": [
                {
                    "description": "clear sky"
                }
            ],
            "main": {
                "temp": 25,
                "feels_like": 26,
                "humidity": 50
            },
            "wind": {
                "speed": 2
            }
        }

        mock_get.return_value = mock_response

        result = WeatherService.get_weather(
            "what is the weather"
        )

        self.assertIn(
            "weather in Bengaluru",
            result
        )

        mock_get.assert_called_once()


    @patch("services.weather_service.Parser.extract_weather_city")
    @patch("services.weather_service.requests.get")
    def test_city_not_found(self, mock_get, mock_city):

        mock_city.return_value = "UnknownCity"

        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = {
            "message": "city not found"
        }

        mock_get.return_value = mock_response

        result = WeatherService.get_weather(
            "weather in UnknownCity"
        )

        self.assertEqual(
            result,
            "I couldn't find weather information for UnknownCity."
        )


    @patch("services.weather_service.Parser.extract_weather_city")
    @patch("services.weather_service.requests.get")
    def test_request_exception(self, mock_get, mock_city):

        mock_city.return_value = "Bangalore"

        import requests

        mock_get.side_effect = requests.exceptions.RequestException(
            "Connection failed"
        )

        result = WeatherService.get_weather(
            "weather in Bangalore"
        )

        self.assertEqual(
            result,
            "Unable to connect to the weather service."
        )


    @patch("services.weather_service.Parser.extract_weather_city")
    @patch("services.weather_service.requests.get")
    def test_invalid_response(self, mock_get, mock_city):

        mock_city.return_value = "Bangalore"

        mock_response = MagicMock()
        mock_response.status_code = 200

        mock_response.json.return_value = {
            "invalid": "data"
        }

        mock_get.return_value = mock_response

        result = WeatherService.get_weather(
            "weather in Bangalore"
        )

        self.assertEqual(
            result,
            "I couldn't retrieve the weather right now. "
            "Please try again later."
        )


if __name__ == "__main__":
    unittest.main()