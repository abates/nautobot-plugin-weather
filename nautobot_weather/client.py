"""Provides weather data based on zipcode."""
import requests


class Client:
    """Obtain local weather information based on zipcode.

    Args:
        zipcode (int): The location's zipcode for weather information.
    """

    def _get_weather_forecast_url(self, latitude, longitude) -> str:
        """Get National Weather Forecast Office forecast url.

        Returns:
            str: URL of the local weather office provided by the latitude and longitude coordinates.
        """
        url = f"https://api.weather.gov/points/{latitude},{longitude}"

        weather_station_data = requests.get(url, timeout=10)
        weather_station_data = weather_station_data.json()

        forecast_url = weather_station_data["properties"]["forecast"]

        return forecast_url

    def _get_weather_data(self, latitude, longitude) -> dict:
        """Get current weather forecast data.

        Returns:
            dict: Dictionary of weather related items.
        """
        # Get weather forecast data.
        forecast_url = self._get_weather_forecast_url(latitude, longitude)
        weather_data = requests.get(forecast_url, timeout=10)
        weather_data = weather_data.json()

        # Get the current weather.
        current_weather = weather_data["properties"]["periods"][0]

        # Dictionary to store all the weather information.
        weather_information = {
            "description": current_weather["name"],
            "short_forecast": current_weather["shortForecast"],
            "detailed_forecast": current_weather["detailedForecast"],
            "temperature": current_weather["temperature"],
            "probability_of_precipitation": current_weather["probabilityOfPrecipitation"]["value"] or 0,
            "temperature_unit": current_weather["temperatureUnit"],
            "wind_speed": current_weather["windSpeed"],
            "wind_direction": current_weather["windDirection"],
        }

        return weather_information
