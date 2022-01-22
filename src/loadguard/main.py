#!/usr/bin/env python3
"""
This module is the LoadGuard Runner entry point.

Module: loadguard.main

This file is a part of LoadGuard Runner.

(c) 2021, Deepnox SAS.
"""

import argparse
import os
import sys
import time

from deepnox import loggers
from loadguard.runner import TasksRunner, ProjectStore

LOGGER = loggers.factory(__name__)
"""The main loggers. """

loggers.setup()


def usage():
    """Print command usage.
    """
    print(
        'loadguard run --project=[loadguard_library] --env=[environment_name] --home=[home_dir] --tasks=[task1][,task2][,...]')


def main():
    """Main program function which parsing provided arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-C', '--container', default=True)
    parser.add_argument('-H', '--home', default=os.environ.get('LG_HOME'))
    parser.add_argument('-e', '--env', default=os.environ.get('LG_ENV') or 'local')
    parser.add_argument('-m', '--exec-mode', default=os.environ.get('LG_MODE') or 'devel')
    parser.add_argument('-p', '--project', default=os.environ.get('LG_PROJECT'))
    parser.add_argument('-t', '--task', default=os.environ.get('LG_TASK') or 'default')
    parser.add_argument('-f', '--func', default=os.environ.get('LG_FUNC') or 'run')
    parser.add_argument('-c', '--config-dir')
    parser.add_argument('-s', '--sources', default=os.environ.get('LG_PROJECT_SOURCES') or "src")


    # parser.add_argument('-v', dest='verbose', action='store_true')
    args: argparse.Namespace = parser.parse_args()

    if None not in [args.home, args.sources]:
        sys.path.insert(0,os.path.join(args.home, args.sources))

    store = ProjectStore(args)
    tasks_runner = TasksRunner(store)

    try:
        LOGGER.debug(f'Running "{args.project}.{args.task}.{args.func}')
        tasks_runner.run(f"{args.project}.{args.task}", args.func)
    except ImportError as e:
        LOGGER.error(f"Import project error", exc_info=e)
        if args.container is True:
            while True: # Container debug mode
                time.sleep(1)
            sys.exit(1)
    except Exception as e:
        print(e)
        LOGGER.error(f"Uncaught error", exc_info=e)
        if args.container is True:
            while True: # Container debug mode
                time.sleep(1)
        sys.exit(1)



if __name__ == '__main__':
    """Program entry point.
    """
    LOGGER.debug('__name__ == __main__')
    main()
