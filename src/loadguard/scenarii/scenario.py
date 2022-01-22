#!/usr/bin/env python3

"""
This module provides tools to create load tests scenarii.

Module: :module:`loadguard.scenarii.scenario`

This file is a part of LoadGuard Runner.

(c) 2021, Deepnox SAS.

"""

import asyncio

from loadguard.scenarii.base import BaseScenario


class LoadTestingScenario(BaseScenario):
    """
    Load testing scenario.
    """

    def __init__(self, loop: asyncio.AbstractEventLoop):
        """
        Instantiate a new :class:`loadguard.scenarii.scenario.LoadTestingScenario`

        :param loop: The event loop.
        :type loop: :class:`asyncio.AbstractEventLoop`
        """
        super().__init__(loop)


