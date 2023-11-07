# jobs.py
from nautobot.extras.jobs import Job
from nautobot.dcim.models import Site

from nautobot_weather.client import Client
from nautobot_weather.models import Weather


class UpdateSiteWeather(Job):
    def update_weather(self, site: Site):
        data = self.client._get_weather_data(site.latitude, site.longitude)
        Weather.objects.update_or_create(
            site=site,
            defaults=data,
        )

    def run(self, data, commit):
        self.client = Client()
        for site in Site.objects.all():
            if site.latitude and site.longitude:
                self.update_weather(site)

jobs = [UpdateSiteWeather]
