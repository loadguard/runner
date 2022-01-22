#!/usr/bin/env python3

"""Unit tests of :class:`loadguard.tests.core.network`.

This file is a part of LoadGuard Runner.

(c) 2021, Deepnox SAS.
"""

import unittest

from deepnox.network.http import HttpMethod


class HttpMethodTest(unittest.TestCase):
    """
    Unit testing: HTTP methods.
    """

    def test___init__(self):
        """
        Test: network methods.
        """
        self.assertIsInstance(HttpMethod.GET, HttpMethod)
        self.assertIsInstance(HttpMethod.POST, HttpMethod)
        self.assertIsInstance(HttpMethod.PUT, HttpMethod)
        self.assertIsInstance(HttpMethod.DELETE, HttpMethod)
        self.assertIsInstance(HttpMethod.HEAD, HttpMethod)
        self.assertIsInstance(HttpMethod.OPTIONS, HttpMethod)
        self.assertIsInstance(HttpMethod.PATCH, HttpMethod)
        self.assertIsInstance(HttpMethod.PATCH, HttpMethod)

    def test__get_method_from_string(self):
        """
        Test: get network method from string.
        :return:
        """
        self.assertEqual(HttpMethod.get('put'), HttpMethod.PUT)
        self.assertEqual(HttpMethod.get('PUT'), HttpMethod.PUT)

        self.assertRaises(AttributeError, lambda: HttpMethod.get('not-existing'))


class HttpHeader(unittest.TestCase):
    """
    Unit testing: HTTP header.
    """

    def test___init__(self):
        """
        Test: network methods.
        """
        self.assertIsInstance(HttpHeader(), HttpHeader)


if __name__ == '__main__':
    """ 
    Entry point. 
    """
    unittest.main()
