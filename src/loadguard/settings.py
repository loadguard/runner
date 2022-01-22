#!/usr/bin/env python3
"""
# loadguard.settings

This file is a part of LoadGuard Runner.

(c) 2021, Deepnox SAS.

This module provides settings management utilities.

"""

import glob
import os
import socket
from http.client import HTTPConnection

import arrow
import shortuuid
import urllib3
import yaml

from deepnox import loggers
from deepnox.third import pydantic

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

LOG = loggers.factory(__name__)

NOW = arrow.now().format('YYYYMMDD-HHmmss')

from jinja2 import Environment, BaseLoader


class Settings(Model):
    pass

class EnvironmentSettings(Settings):
    """
    Environment settings.
    """
    def __init__(self, home: str):
        self._home = os.environ.get("LG_HOME")
        """ The LG_HOME corresponding to root path of runner. """
        if not self._home: raise ValueError(
            f"LG_HOME environment variable is mandatory. Please set using command: export LG_HOME=\"/path/to/runner\"")


def global_settings(home: str, env: str):
    LOG.debug(f'global_settings(home={home}, env={env})')
    configuration = {}
    configuration.HOSTNAME = socket.gethostname().lower()
    # Specified environment.
    configuration.LG_ENV = env or os.environ.get(
        'LG_ENV') or configuration.HOSTNAME

    # LoadGuard home path.
    configuration.LG_HOME = home or os.path.abspath(
        os.environ.get('LG_HOME')) or '/loadguard'

    # Configuration directory.
    configuration.LG_CONF_DIR = os.environ.get('LG_HOME')

    # Specific environment configuration directory.
    configuration.LG_ENV_DIR = os.path.join(
        configuration.LG_CONF_DIR, 'conf')

    # Absolute path of environment file depending of machine.
    configuration.LG_ENV_FILE = os.path.join(
        configuration.LG_CONF_DIR, '{}'.format(
            configuration.LG_ENV))

    # Log level.
    configuration.LG_LOGLEVEL = os.environ.get('LG_LOGLEVEL') or 'DEBUG'
    configuration.LG_LOGLEVEL = configuration.LG_LOGLEVEL.upper()

    # Dataset directory.
    configuration.LG_DATASET_DIR = os.path.join(
        configuration.LG_HOME, 'datasets')

    # Templates directory.
    configuration.LG_TEMPLATES_DIR = os.path.join(
        configuration.LG_HOME, 'project/templates')

    # Logs directory.
    configuration.LG_LOG_DIR = os.path.join(
        configuration.LG_HOME, 'project/logs')


    # Test results directory.
    configuration.LG_TEST_RESULTS_DIR = os.path.join(
        configuration.LG_HOME, 'test_results')

    return configuration


def project_settings(global_settings):
    """
    Load settings for project and specified environement.

    :param global_settings:
    :return:
    """
    configuration = {}
    files_pattern = os.path.join(
        global_settings.LG_CONF_DIR,
        global_settings.LG_ENV,
        '*.yml')
    LOG.debug(f'file_pattern={files_pattern}',
              extra={'file_pattern': files_pattern})
    files = glob.glob(files_pattern)
    LOG.debug(f'files',
              extra={'files': files})
    for file in files:
        LOG.debug(f'Parsing file: {file}', extra={'file': file})
        template = Environment(loader=BaseLoader()).from_string('\n'.join(open(file).readlines()))
        res = template.render({'now': NOW, 'LG_HOME': global_settings.LG_HOME})
        configuration.update(yaml.safe_load(res))
        LOG.debug('configuration', extra=configuration)
        configuration.update(
            {'metadata': {'uid': shortuuid.ShortUUID().random(length=16)}})
    LOG.debug('Final computed settings for project', extra={'configuration': configuration})
    o = Map({})
    o.update(configuration)
    try:
        loggers.setup(o.logging)
    except KeyError:
        loggers.setup()
    try:
        HTTPConnection.debuglevel = o.http_connection.get('debuglevel')
    except:
        pass
    return o
