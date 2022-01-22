#!/usr/bin/env python3
"""
# loadguard.project.template

This file is a part of LoadGuard Runner.

(c) 2021, Deepnox SAS.

This module provides template utilities.

"""

import jinja2
import yaml


templateLoader = jinja2.FileSystemLoader(searchpath=SETTINGS.LG_TEMPLATES_DIR)
templateEnv = jinja2.Environment(loader=templateLoader, autoescape=True)


def render(short_name: str, data: dict) -> dict:
    """Get request body as JSON from YAML template.

    :param: short_name - Template name without path and extension.
    :param: data - Context dictionary.
    :return: Request body as JSON
    """
    template = templateEnv.get_template('{}.yml.j2'.format(short_name))
    yaml_body = template.render(data)
    # loggers.debug(yaml_body)
    return yaml.safe_load(yaml_body, Loader=yaml.BaseLoader)
