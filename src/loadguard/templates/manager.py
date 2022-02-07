#!/usr/bin/env python3

"""
This module provides a templates manager.

Package: loadguard.templates

This file is a part of LoadGuard Runner.

(c) 2022, Deepnox SAS.

"""
import os
from typing import Any

from jinja2 import FileSystemLoader, Environment, BaseLoader


class TemplatesManager(object):
    """
    Template manager.

    """

    def __init__(self, path: str = None):
        """
        Create a new instance of :class:`loadguard.templates.TemplatesManager`
        :param path: The path to lookup.
        :type path: str
        """
        self.base_env, self.file_env = Environment(loader=BaseLoader), None

        if path:
            file_loader = FileSystemLoader(path)
            self.file_env = Environment(loader=file_loader)


    def render(self, template_obj: str, ctx: Any = None):
        """
        Render a template using the provided context.

        :param template_obj: The template file.
        :type template_obj: str
        :param ctx: The context.
        :type ctx: :class:`typing.Any`
        :return: The rendering.
        :rtype: str
        """
        if self.file_env is not None and os.path.exists(template_obj):
            template = self.file_env.get_template(template_obj)
        else:
            template = self.base_env.from_string(template_obj)
        return template.render(ctx)
