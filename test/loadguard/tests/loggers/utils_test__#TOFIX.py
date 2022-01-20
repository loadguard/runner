#!/usr/bin/env python3
import logging

from deepnox import loggers
from deepnox.helpers.testing_helpers import BaseTestCase


class LoadGuardLoggerTestCase(BaseTestCase):
    """
    LoadGuardLogger unit tests.

    """

    def test____init__(self):
        logger = LoadGuardLogger()
        self.assertIsInstance(logger, LoadGuardLogger)
        self.assertIsInstance(logger._logger, logging.Logger)

    def test_default_logging_info(self):
        logger = LoadGuardLogger()
        def fn_testing_default_logging_info():
            logger.info('Info loggers using default loggers')

        with self.assertLogs() as captured:
            fn_testing_default_logging_info()
        self.assertEqual(len(captured.records), 1)  # check that there is only one loggers message
        self.assertEqual(captured.records[0].getMessage(), 'Info loggers using default loggers')  # and it is the proper one
        self.assertEqual(captured.records[0].levelname, 'INFO')
        print(captured.records[0].pathname)

    def test_default_logging_info_with_extra(self):
        logger = LoadGuardLogger()
        loggers.setup()
        def fn_testing_default_logging_info():
            logger.info('Info loggers using default loggers with extra', extra={'key_test': 'value_test'})

        with self.assertLogs() as captured:
            fn_testing_default_logging_info()
        self.assertEqual(len(captured.records), 1)  # check that there is only one loggers message
        self.assertEqual(captured.records[0].getMessage(), 'Info loggers using default loggers with extra')  # and it is the proper one
        self.assertEqual(captured.records[0].levelname, 'INFO')
        #self.assertNotRaises(None, json.loads(str(captured.records[0])))
        print('---', captured.records[0])
        for o in dir(captured.records[0]):
            print(o)
