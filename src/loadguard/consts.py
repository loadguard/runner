#!/usr/bin/env python3
"""
This module is containing common constants.

Module: loadguard.constants

This file is a part of LoadGuard Runner.

(c) 2021, Deepnox SAS.
"""
from deepnox import loggers

LOAD_TESTS_METRICS_LOGGER = loggers.factory("loadguard.audit.load_tests.metrics")

LG_PROJECT_CONFIGURATION_DEFAULT_FILENAME: str = "loadguard-project.yml"
""" The default filename of a LoadGuard project configuration. """