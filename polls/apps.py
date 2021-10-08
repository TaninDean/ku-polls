"""Module of django to find config."""
from django.apps import AppConfig


class PollsConfig(AppConfig):
    """Class to find database."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
