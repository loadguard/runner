#!/usr/bin/env python3

"""
Unit tests for module: loadguard.stores.project_store

This file is a part of LoadGuard project.

(c) 2021, Deepnox SAS.
"""

import unittest

from deepnox.tests.helpers.filesystem import TestFileContent
from deepnox.utils.maps import Map
from loadguard.stores.project_store import ProjectStore


class ProjectStoreTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self._configuration_file = TestFileContent("""---
            key1: value1
            key2: 1.42
            """)

    def test_error_if_any_argument_is_provided(self):
        self.assertRaises(ValueError, lambda: ProjectStore())
        self.assertRaises(TypeError, lambda: ProjectStore('string_test'))

    def test__create_a_valid_instance_of_project_store(self):
        args = Map(project="project.test", environment="performance_test", config_dir="/my/config/dir")
        store = ProjectStore(args)
        self.assertIsInstance(store, ProjectStore)

if __name__ == '__main__':
    unittest.main()
