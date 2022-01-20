#!/usr/bin/env python3

"""
This module provides tools to create load tests scenarii.

Module: :module:`loadguard.scenarii.scenario_http`

This file is a part of LoadGuard Runner.

(c) 2021, Deepnox SAS.

"""

import asyncio
from concurrent.futures import ProcessPoolExecutor

import aiohttp

from deepnox.clients.http_client import HttpClient
from loadguard.scenarii.base import BaseScenario
from loadguard.scenarii.scenario import LoadTestingScenario


class HttpLoadTestingScenario(LoadTestingScenario):
    """
    Load testing scenario.
    """

    def __init__(self,
                 loop: asyncio.AbstractEventLoop = None,
                 http_client: HttpClient = None,
                 ):
        """
        Instantiate a new :class:`loadguard.scenarii.scenario.LoadTestingScenario`

        :param loop: The event loop.
        :type loop: :class:`asyncio.AbstractEventLoop`
        """
        super().__init__(loop)
        self.http_client = http_client

    async def run(self, fn, timeout: int = 30):
        ex = ProcessPoolExecutor(2)
        await self.loop.run_in_executor(ex, fn, 11)
