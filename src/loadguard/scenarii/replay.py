#!/usr/bin/env python3

"""
This module provides tools to create load tests user_scenarii.

Module: :module:`loadguard.user_scenarii.replay`

This file is a part of LoadGuard Runner.

(c) 2021, Deepnox SAS.

"""
import asyncio
from typing import Dict, Union

from deepnox import loggers
from deepnox.clients.http_client import HttpClient
from deepnox.network.http import HttpRequest

LOGGER = loggers.factory(__name__)
""" The main logger of :module:`loadguard.user_scenarii.replay`. """


class HttpRequestReplay(HttpClient):
    """
    Replay a HTTP request.

    """

    LOG = LOGGER.getChild('ReplayHttpRequest')
    """ The main logger of :class:`loadguard.user_scenarii.replay.ReplayHttpRequest`. """

    def __init__(self,
                 loop: asyncio.AbstractEventLoop = None,
                 auditor_logger=None,
                 timeout: int = 30,
                 verify_ssl: bool = False
                 ):
        """
        Create a new instance of :class:`loadguard.user_scenarii.replay.ReplayHttpRequest` to
        replay :class:`deepnox.network.http.HttpRequest`.

        :param loop: The event loop.
        :type loop: :class:`asyncio.AbstractEventLoop`
        :param auditor_logger: The logger used for auditing.
        :type auditor_logger:
        :param timeout: The request timeout.
        :type timeout: int
        :param verify_ssl: Should I verify TLS/SSL certificate?
        :type verify_ssl: bool
        """
        super().__init__(loop=loop, auditor_logger=auditor_logger, timeout=timeout, verify_ssl=verify_ssl)

    async def replay(self, req: Union[HttpRequest, Dict]):
        """
        Replay the provided HTTP request.

        :param req: The HTTP request
        :type req: Union[HttpRequest, Dict]
        :return:
        """
        self.LOG.debug(f"replay(req={req})", extra={"req": req})
        if not isinstance(req, (HttpRequest, dict)):
            raise TypeError(
                f"Attribute named `request` must be typed HttpRequest or dict: (type(request)={type(req)}")
        return await self.request(req)
