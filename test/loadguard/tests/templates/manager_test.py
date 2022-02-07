#!/usr/bin/env python3

"""
Unit tests: template manager.

Package: :module:`loadguard.tests.templates.manager_test`

This file is a part of LoadGuard Runner.

(c) 2021, Deepnox SAS.

"""

import unittest
from unittest import mock

from deepnox.helpers.testing_helpers import BaseTestCase
from loadguard.templates.manager import TemplatesManager


class TemplatesManagerTestCase(BaseTestCase):
    """
    Test cases of :class:`loadguard.templates.manager.TemplatesManager`
    """

    @mock.patch('loadguard.templates.manager.os.path')
    def test__create_an_instance_using_valid_directory_should_be_okay(self, mock_path):
        mock_path.isdir.return_value = True
        self.assertIsInstance(TemplatesManager(path="/fake/valid/directory"), TemplatesManager)

    @mock.patch('loadguard.templates.manager.os.path')
    def _test__create_an_instance_using_invalid_directory_should_raise_an_error(self, mock_path):
        """
        :todo: Unit test.

        :param mock_path:
        :return:
        """
        mock_path.isdir.return_value = False
        self.assertRaises(AttributeError, lambda: TemplatesManager(path="/fake/invalid/directory"))

    # @mock.patch('jinja2.environment.os.path')
    # @mock.patch('loadguard.templates.manager.os.path')
    # def test__render_using_an_existing_file_should_be_okay(self, mock_path_loadguard, mock_path_jinja2):
    #     mock_path_loadguard.isdir.return_value = True
    #     mock_path_jinja2.isfile.return_value = True
    #     manager = TemplatesManager(path="/fake/valid/directory")
    #     manager.render("existing-template", {})


if __name__ == '__main__':
    unittest.main()
