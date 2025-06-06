from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ExamplesAppConfig(AppConfig):
    """Default configuration for Examples app."""

    name = "apps.examples"
    verbose_name = _("Examples")