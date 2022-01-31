#!/usr/bin/env python3

"""
Unit tests for module: loadguard.tests.user_scenarii.base_test

This file is a part of LoadGuard project.

(c) 2021, Deepnox SAS.
"""

import unittest

from deepnox.helpers.testing_helpers import BaseAsyncTestCase
from loadguard.scenarii.replay import HttpRequestReplay


class HttpRequestReplayTestCase(BaseAsyncTestCase):
    """
    Test case for base scenario.
    """

    def test__create_a_valid_instance(self):
        """
        Tests: create a new instance of scenario.
        """
        self.assertIsInstance(HttpRequestReplay(self.loop), HttpRequestReplay)

    def test__create_a_valid_instance_should_raise_an_error(self):
        """
        Tests: try to create an instance using invalid parameters.
        """
        self.assertRaises(TypeError, lambda: HttpRequestReplay(heurk=1))


if __name__ == '__main__':
    unittest.main()
