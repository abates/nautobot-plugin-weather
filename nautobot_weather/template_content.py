from nautobot.apps.ui import TemplateExtension

from .models import Weather


class SiteWeather(TemplateExtension):
    """Add current weather panel to sites."""

    model = 'dcim.site'

    def right_page(self):
        if self.context["object"].latitude and self.context["object"].longitude:
            return self.render('nautobot_weather/site_weather_panel.html', extra_context={
                "weather": Weather.objects.get(site=self.context["object"]),
            })
        return None


template_extensions = [SiteWeather]
