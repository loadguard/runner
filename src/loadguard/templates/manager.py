#!/usr/bin/env python3

"""
This module provides a templates manager.

Package: loadguard.templates

This file is a part of LoadGuard Runner.

(c) 2022, Deepnox SAS.

"""
import os
from typing import Any

from jinja2 import FileSystemLoader, Environment



class TemplatesManager(object):
    """
    Template manager.

    """

    def __init__(self, path: str):
        """
        Create a new instance of :class:`loadguard.templates.TemplatesManager`
        :param path: The path to lookup.
        :type path: str
        """
        if not os.path.isdir(path):
            raise AttributeError(f"Path is missing: {path}")
        file_loader = FileSystemLoader(path)
        self.env = Environment(loader=file_loader)

    def render(self, template_file: str, ctx: Any = None):
        """
        Render a template using the provided context.

        :param template_file: The template file.
        :type template_file: str
        :param ctx: The context.
        :type ctx: :class:`typing.Any`
        :return: The rendering.
        :rtype: str
        """
        template = self.env.get_template(template_file)
        return template.render(ctx)
