#!/usr/bin/env python3

"""
Unit tests for module: loadguard.tests.user_scenarii.base_test

This file is a part of LoadGuard project.

(c) 2021, Deepnox SAS.
"""
import asyncio
import unittest

import aiohttp

from deepnox.helpers.testing_helpers import BaseAsyncTestCase
from loadguard.scenarii.base import BaseScenario
from loadguard.scenarii.scenario_http import HttpLoadTestingScenario


class BaseScenarioTestCase(BaseAsyncTestCase):
    """
    Test case for base scenario.
    """

    def test__create_a_valid_instance(self):
        """
        Tests: create a new instance of scenario.
        """
        self.assertIsInstance(HttpLoadTestingScenario(self.loop), BaseScenario)
        self.assertIsInstance(HttpLoadTestingScenario(self.loop), HttpLoadTestingScenario)

    def test__session(self):
        """
        Tests: get client session.
        """
        scenario = HttpLoadTestingScenario(self.loop)
        self.assertIsInstance(scenario.session(), aiohttp.ClientSession)


if __name__ == '__main__':
    unittest.main()
