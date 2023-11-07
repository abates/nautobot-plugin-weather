# models.py
from django.db import models
from django.core.exceptions import ValidationError

from nautobot.apps.models import PrimaryModel

from .client import Client


class Weather(PrimaryModel):
    """Base model for animals."""

    site = models.OneToOneField(to="dcim.Site", on_delete=models.CASCADE, null=True)
    forecast_url = models.URLField(blank=True, null=True)

    description = models.CharField(verbose_name="Description", max_length=50)
    short_forecast = models.CharField(verbose_name="Short Forecast", max_length=255)
    detailed_forecast = models.TextField(verbose_name="Detailed Forecast")
    temperature = models.IntegerField(verbose_name="Temperature")
    probability_of_precipitation = models.IntegerField(verbose_name="Probability of Precipitation", default=0)
    temperature_unit = models.CharField(verbose_name="Temperature Unit", max_length=1)
    wind_speed = models.CharField(verbose_name="Wind Speed", max_length=255)
    wind_direction = models.CharField(verbose_name="Wind Direction", max_length=2)

    def clean(self):
        if self.site.latitude is None or self.site.longitude is None:
            raise ValidationError({"site": "Site latitude and longitude must be set"})

    def update(self):
        client = Client()
        if not self.forecast_url:
            client = Client()
            self.forecast_url = client.get_weather_forecast_url(self.site.latitude, self.site.longitude)

        data = client.get_weather_data(self.forecast_url)
        for attr, value in data.items():
            setattr(self, attr, value)

    def __str__(self):
        return self.short_forecast
