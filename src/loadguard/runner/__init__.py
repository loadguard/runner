#!/usr/bin/env python3

"""
Package: :module:`loadguard.runners.__init__`

This file is a part of LoadGuard Runner.

(c) 2021, Deepnox SAS.


"""

__import__("pkg_resources").declare_namespace(__name__)


import importlib
import inspect
import json
import logging
from types import ModuleType

import arrow

from loadguard.stores.project_store import ProjectStore

LOGGER = logging.getLogger(__name__)
"""The main loggers. """

NOW = arrow.now().format('YYYYMMDD-HHmmss')


class TasksRunner(object):
    """
    Run a task.
    """

    LOG = LOGGER.getChild('TasksRunner')
    """The loggers. """

    _store: ProjectStore = None
    """The project store. """

    def __init__(self, store: ProjectStore):
        """
        Create a new instance of :class:`loadguard.runner.TasksRunner`.

        :param store: The project store.
        :type store: SettingsProjectStore
        """
        self.LOG.debug('__init__()', extra={'store': store})
        self._store: ProjectStore = store
        self._main_module_name: str = self.load_module(store.ARGS.project)
        if not self._main_module_name:
            raise Exception(f'Unable to load project: {store.ARGS.project}')

    def load_module(self, py_module_name: str) -> ModuleType:
        """
        Importing module to load task of project.

        :param py_module_name: The Python module name.
        :type py_module_name: str
        """
        self.LOG.debug('load_module()', extra={'task': py_module_name})
        if py_module_name is None or not isinstance(py_module_name, str):
            raise AttributeError(
                f'Argument is `None` or invalid: (task={py_module_name})')
        return importlib.import_module(py_module_name)

    def get_user_classes(self) -> list:
        """
        Return user classes of module.

        :return: List of user classes.
        :rtype: list
        """
        self.LOG.debug('get_user_classes()')
        return [obj for name, obj in inspect.getmembers(
            self._py_module) if inspect.isclass(obj)]

    def run(self, task: str, func: str) -> ProjectStore:
        """
        Run a project task.

        :param task: Python module name.
        :type task: str
        :return: The completed project store.
        :rtype: SettingsProjectStore
        """
        self.LOG.debug('run_task()', {'task': task})
        if not isinstance(self._store, ProjectStore):
            raise TypeError(
                f'`store` must be an instance of `SettingsProjectStore`: (store={self._store})')
        try:
            m = self.load_module(task)
        except Exception as e:
            raise ImportError(f'Unable to import {task}', e)
        run_func = getattr(m, func)
        if not run_func:
            raise KeyError(f'Missing `{func}` function in {task}')
        result = run_func(self._store)
        if not isinstance(result, ProjectStore):
            raise TypeError(
                f'Hit of running function must be an instance of `SettingsProjectStore`: {type(result)}')
        return result

    def run_sequence(self, tasks: list) -> ProjectStore:
        """
        Run a sequence of tasks.

        :param tasks: Tasks list to run.
        :type tasks: list
        :return: The completed project store.
        :rtype: SettingsProjectStore
        """
        self.LOG.debug('run_tasks_sequence()', extra={'tasks': tasks})
        for task in tasks:
            self.LOG.info(f'Running task: {task}', extra={'task': task})
            self._store = self.run(task)
        return self

    @property
    def store(self) -> ProjectStore:
        """
        Return project store.
        """
        return self._store

#
# class LoadTestsRunner(TasksRunner):
#     LOGGER = LOGGER.getChild('LoadTestsRunner')
#
#     def __init__(self, py_module_name):
#         """Create a new instance of {LoadTestsRunner}.
#         """
#         self.LOGGER.debug('__init__(self, task={})'.format(py_module_name),
#                        extra={'task': py_module_name})
#         super().__init__(py_module_name=py_module_name)
#
#     def start_test(self, user_count: int = 1, spawn_rate: int = 1, spawn_later: int = 1):
#         raise NotImplemented('start_test() is not implemented')
#
#     def start_tests_loop(self, scenarios: list):
#         raise NotImplemented('start_tests_loop() is not implemented')
