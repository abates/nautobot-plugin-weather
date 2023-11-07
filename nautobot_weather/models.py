# models.py
from django.db import models

from nautobot.apps.models import PrimaryModel


class Weather(PrimaryModel):
    """Base model for animals."""

    site = models.OneToOneField(to="dcim.Site", on_delete=models.CASCADE, null=True)

    description = models.CharField(verbose_name="Description", max_length=50)
    short_forecast = models.CharField(verbose_name="Short Forecast", max_length=255)
    detailed_forecast = models.TextField(verbose_name="Detailed Forecast")
    temperature = models.IntegerField(verbose_name="Temperature")
    probability_of_precipitation = models.IntegerField(verbose_name="Probability of Precipitation", default=0)
    temperature_unit = models.CharField(verbose_name="Temperature Unit", max_length=1)
    wind_speed = models.CharField(verbose_name="Wind Speed", max_length=255)
    wind_direction = models.CharField(verbose_name="Wind Direction", max_length=2)

    def __str__(self):
        return self.short_forecast
