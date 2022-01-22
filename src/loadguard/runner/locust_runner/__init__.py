#!/usr/bin/env python3
"""
# loadguard.runner.locust_runner

This file is a part of LoadGuard Runner.

(c) 2021, Deepnox SAS.

This module provides a generic access to REST API.

"""

import logging

import gevent
from locust import HttpUser
from locust.env import Environment
from locust.stats import stats_history

from loadguard.runner import TasksRunner


class LocustLoadTestsRunner(TasksRunner):
    """A runner for Locust load tests."""

    def __init__(self, py_module: str):
        """ Create a new instance of :class:``.

        :param py_module: The name of Python module.
        :type py_module: str
        """
        super().__init__(py_module_name=py_module)
        self.user_classes = self.get_user_classes()
        logging.info(
            'self.user_classes', extra={
                'self.user_classes': [
                    x.__class__.__name__ for x in self.user_classes]})
        self.env = Environment(user_classes=self.user_classes)

    def get_user_classes(self):
        """ Returns user classes. """
        return list(
            filter(
                lambda o: issubclass(
                    o,
                    HttpUser) and not isinstance(
                    o,
                    HttpUser),
                super().get_user_classes()))

    def start_test(
            self,
            user_count: int = 1,
            spawn_rate: int = 1,
            spawn_later: int = 1):
        """Start a load tests. """
        self.env.create_local_runner()
        # start a greenlet that periodically outputs the current stats
        # gevent.spawn(stats_printer(env.stats))
        # start a greenlet that save current stats to history
        gevent.spawn(stats_history, self.env.runner)
        # start the tests
        self.env.runner.start(user_count, spawn_rate=spawn_rate)
        gevent.spawn_later(spawn_later, lambda: self.env.runner.quit())
        # wait for the greenlets
        self.env.runner.greenlet.join()
        return self

    def start_tests_loop(self, scenarios: list):
        """Start multiple tests. """
        if not scenarios:
            logging.warn('No scenario provided.')
            return
        for scenario in scenarios:
            self.start_test(user_count=scenario.get('user_count'),
                            spawn_rate=scenario.get('spawn_rate'),
                            spawn_later=scenario.get('spawn_later'))
