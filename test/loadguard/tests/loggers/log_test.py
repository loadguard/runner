#!/usr/bin/env python3

import logging
import unittest

from deepnox import loggers


class LoggersTestCase(unittest.TestCase):
    """
    Loggz unit tests.

    """

    def test_factory__create_logger(self):
        logger = loggers.factory('logger_test')
        self.assertIsInstance(logger, logging.Logger)

    def test_factory__create_child_logger(self):
        logger = loggers.factory('logger_test', 'child_test')
        self.assertIsInstance(logger, logging.Logger)

    def test_default_logging_info(self):
        def fn_testing_default_logging_info():
            logging.info('Info loggers using default loggers')

        with self.assertLogs() as captured:
            fn_testing_default_logging_info()
        self.assertEqual(len(captured.records), 1)  # check that there is only one loggers message
        self.assertEqual(captured.records[0].getMessage(), 'Info loggers using default loggers')  # and it is the proper one
        self.assertEqual(captured.records[0].levelname, 'INFO')
        print(captured.records[0].pathname)

    def test_custom_logger_info(self):
        def fn_testing_custom_logger_info():
            LOG = loggers.factory(__name__)
            LOG.info('Info loggers using custom loggers')

        with self.assertLogs() as captured:
            fn_testing_custom_logger_info()
        self.assertEqual(len(captured.records), 1)  # check that there is only one loggers message
        self.assertEqual(captured.records[0].getMessage(), 'Info loggers using custom loggers')  # and it is the proper one
        self.assertEqual(captured.records[0].levelname, 'INFO')
        self.assertEqual(captured.records[0].name, __name__)
