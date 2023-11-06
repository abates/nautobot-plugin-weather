"""Plugin declaration for nautobot_weather."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
try:
    from importlib import metadata
except ImportError:
    # Python version < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)

from nautobot.extras.plugins import NautobotAppConfig


class NautobotWeatherConfig(NautobotAppConfig):
    """Plugin configuration for the nautobot_weather plugin."""

    name = "nautobot_weather"
    verbose_name = "Nautobot Weather"
    version = __version__
    author = "Andrew Bates"
    description = "Nautobot Weather."
    base_url = "nautobot-weather"
    required_settings = []
    min_version = "1.6.0"
    max_version = "1.9999"
    default_settings = {}
    caching_config = {}


config = NautobotWeatherConfig  # pylint:disable=invalid-name
