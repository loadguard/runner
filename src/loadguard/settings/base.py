#!/usr/bin/env python3

"""
# Module: loadguard.settings.base

This file is a part of LoadGuard Runner.

(c) 2021, Deepnox SAS.

"""


from deepnox import loggers
from deepnox.settings.base import SettingsReader


LOGGER = loggers.factory(__name__)
""" The module logger. """


class ProjectSettings(SettingsReader):
    """
    A class to manage project settings.
    """

    def __init__(self, filename: str = None):
        """
        Create a new settings object from provided LoadGuard project configuration (a YAML file).
        :param filename: The configuration filename.
        """
        super().__init__(filename=filename)


class LoggingSettings(SettingsReader):
    """
    A class to manage logging settings.

    :todo: check if schema is valid!
    """

    def __init__(self, filename: str = None):
        """
        Create a new settings object from provided LoadGuard project configuration (a YAML file).
        :param filename: The configuration filename.
        """
        super().__init__(filename=filename)
