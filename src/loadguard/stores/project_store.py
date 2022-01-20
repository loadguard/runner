#!/usr/bin/env python3

"""
# loadguard.runner.store

This module provides a useful store to run a LoadGuard project sequence.

"""
import asyncio
import importlib
import inspect
import logging
import os
from argparse import Namespace
from types import ModuleType

import arrow

from deepnox.settings.base import read_yaml_file
from deepnox.utils.maps import UpperMap, Map

LOGGER = logging.getLogger(__name__)
"""The main loggers. """

NOW = arrow.now().format('YYYYMMDD-HHmmss')


class ProjectStore(UpperMap):
    """
    A project store to pass data between tasks.

    :todo: https://stackoverflow.com/a/39716001
    """

    LOG = LOGGER.getChild('ProjectStore')
    """The logger. """

    def __init__(self, args: Namespace = None):
        """
        Create a new instance of {TasksStore}.

        :param project: The LoadGuard project name.
        :param env: Environment name.
        :param home: LoadGuard project home.
        """
        self.LOG.debug(f'__init__(args={args})')
        if args is None:
            raise ValueError(f"Creating a `{self.__class__.__name__}` needs arguments (home, project, env, config-dir)")

        if not isinstance(args, (Namespace, Map)):
            raise TypeError(f"Creating a `{self.__class__.__name__}` needs a typed <argparse.Namespace> argument")

        project_configuration_filename = "loadguard-project.yml"
        print("config", args.config_dir)
        settings_filename = os.path.join(args.config_dir, project_configuration_filename)
        self['config'] = {
            "dir": args.config_dir,
            "filename": project_configuration_filename,
        }
        del args.config_dir
        for arg in dir(args):
            self[arg] = getattr(args, arg)

        self.LOG.error("settings_filename", extra={"settings_filename": settings_filename})

        self.SETTINGS = UpperMap(read_yaml_file(settings_filename))
        self.DATA = UpperMap()
        self._loop: asyncio.AbstractEventLoop = None

    @property
    def loop(self):
        return asyncio.get_event_loop()


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
        :type store: ProjectStore
        """
        self.LOG.debug('__init__()', extra={'store': store})
        self._store: ProjectStore = store
        self._main_module_name: str = self.load_module(store.PROJECT)
        if not self._main_module_name:
            raise Exception(f'Unable to load project: {store.PROJECT}')

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

    def run(self, task: str) -> ProjectStore:
        """
        Run a project task.

        :param task: Python module name.
        :type task: str
        :return: The completed project store.
        :rtype: ProjectStore
        """
        self.LOG.debug('run_task()', {'task': task})
        if not isinstance(self._store, ProjectStore):
            raise TypeError(
                f'`store` must be an instance of `ProjectStore`: (store={self._store})')
        try:
            m = self.load_module(task)
        except Exception as e:
            raise ImportError(f'Unable to import {task}', e)
        run_func = getattr(m, 'run')
        if not run_func:
            raise KeyError(f'Missing `run` function in {task}')
        result = run_func(self._store)

        if not isinstance(result, ProjectStore):
            raise TypeError(
                f'Hit of running function must be an instance of `ProjectStore`: {type(result)}')
        return result

    def run_sequence(self, tasks: list) -> ProjectStore:
        """
        Run a sequence of tasks.

        :param tasks: Tasks list to run.
        :type tasks: list
        :return: The completed project store.
        :rtype: ProjectStore
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
