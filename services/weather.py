import os
from urllib import response
import requests
from dotenv import load_dotenv

from core.parser import Parser

load_dotenv()



class WeatherService:

    @staticmethod
    def get_weather(command):

        city = Parser.extract_weather_city(command)

        if not city:
            city = "Bengaluru"

        api_key = os.getenv("WEATHER_API_KEY")

        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}"
            f"&appid={api_key}"
            "&units=metric"
        )

        try:

            response = requests.get(url, timeout=10)
            data = response.json()

            if response.status_code != 200:
                return f"I couldn't find weather information for {city}."

            weather = data["weather"][0]["description"].title()
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            return (
                f"The weather in {city} is {weather}. "
                f"The temperature is {temperature} degrees Celsius, "
                f"feels like {feels_like} degrees, "
                f"humidity is {humidity} percent, "
                f"and wind speed is {wind} meters per second."
            )

        except requests.exceptions.RequestException:
            return "Unable to connect to the weather service."

        except Exception as e:
            logger.error("Weather", e)
            return (
                "I couldn't retrieve the weather right now. "
                "Please try again later."
            )