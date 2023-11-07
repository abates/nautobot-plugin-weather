"""Provides weather data based on zipcode."""
import requests
from requests.adapters import HTTPAdapter, Retry


class Client:
    """Simple API client for NWS weather forecast data."""

    def __init__(self):
        self.session = requests.Session()
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
        self.session.mount('http://', HTTPAdapter(max_retries=retries))

    def get_weather_forecast_url(self, latitude, longitude) -> str:
        """Get National Weather Forecast Office forecast url.

        Returns:
            str: URL of the local weather office provided by the latitude and longitude coordinates.
        """
        lookup_url = f"https://api.weather.gov/points/{latitude},{longitude}"

        response = self.session.get(lookup_url, timeout=10)
        weather_station_data = response.json()

        return weather_station_data["properties"]["forecast"]

    def get_weather_data(self, forecast_url) -> dict:
        """Get current weather forecast data.

        Returns:
            dict: Dictionary of weather related items.
        """
        # Get weather forecast data.
        response = self.session.get(forecast_url, timeout=10)
        weather_data = response.json()

        # Get the current weather.
        current_weather = weather_data["properties"]["periods"][0]

        return {
            "description": current_weather["name"],
            "short_forecast": current_weather["shortForecast"],
            "detailed_forecast": current_weather["detailedForecast"],
            "temperature": current_weather["temperature"],
            "probability_of_precipitation": current_weather["probabilityOfPrecipitation"]["value"] or 0,
            "temperature_unit": current_weather["temperatureUnit"],
            "wind_speed": current_weather["windSpeed"],
            "wind_direction": current_weather["windDirection"],
        }
