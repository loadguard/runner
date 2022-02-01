#!/usr/bin/env python3

"""
# loadguard.stores

This module provides a useful store to run a LoadGuard project sequence.

This file is a part of LoadGuard Runner.

(c) 2021, Deepnox SAS.
"""

import asyncio
import importlib
import inspect
import logging
import os
from argparse import Namespace
from types import ModuleType

import arrow

from deepnox.settings.base import load_settings
from deepnox.utils.maps import Map
from loadguard.consts import LG_PROJECT_CONFIGURATION_DEFAULT_FILENAME

LOGGER = logging.getLogger(__name__)
"""The main loggers. """

NOW = arrow.now().format('YYYYMMDD-HHmmss')


class ProjectStore(Map):
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

        self.ARGS = ProjectStore.get_project_args(args)
        self.PATHS = ProjectStore.get_project_paths(self.ARGS.project_root, self.ARGS.env)
        self.PATHS.settings_file = os.path.join(self.PATHS.config_dir, LG_PROJECT_CONFIGURATION_DEFAULT_FILENAME)
        self.SETTINGS = load_settings(self.PATHS.settings_file).get()
        self.DATA = Map()
        self._loop: asyncio.AbstractEventLoop = None

    @staticmethod
    def get_project_paths(project_root: str, env: str):
        """
        Returns the usable paths by the current LoadGuard project.

        :param project_root: The root path of project
        :type project_root: str
        :return: The usable paths by the project.
        """
        return Map({"src": os.environ.get("LG_PROJECT_SRC_DIR", os.path.join(project_root, "src")),
                    "test": os.environ.get("LG_PROJECT_TEST_DIR", os.path.join(project_root, "test")),
                    "config": os.environ.get("LG_PROJECT_CONFIG_DIR", os.path.join(project_root, "config", env)),
                    "deploy": os.environ.get("LG_PROJECT_TEST_DIR", os.path.join(project_root, "deploy", env)),
                    "templates": os.environ.get("LG_PROJECT_TEMPLATES_DIR",
                                                os.path.join(project_root, "res", "templates")),
                    "datasets": os.environ.get("LG_PROJECT_DATASETS_DIR",
                                                os.path.join(project_root, "res", "datasets"))}
                   )

    @staticmethod
    def get_project_args(args):
        """
        Returns projects arguments as dict.

        :param args: The arguments.
        :return: The arguments as dict.
        :rtype: Map
        """
        return Map({arg: getattr(args, arg) for arg in dir(args)})

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
        self._package = self.load_module(store.project)
        self._store.project_home = os.path.abspath(self._package.__file__)
        if not self._package:
            raise Exception(f'Unable to load project: {store.PROJECT}')

    def load_module(self, py_module_name: str) -> ModuleType:
        """
        Importing module to load task of project.

        :param py_module_name: The Python module name.
        :type py_module_name: str
        """
        self.LOG.debug('load_module()', extra={'py_module_name': py_module_name})
        if py_module_name is None or not isinstance(py_module_name, str):
            raise AttributeError(
                f'Argument is `None` or invalid: (py_module_name={py_module_name})')
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
        self.LOG.debug('run(task: str)', {'task': task})
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
