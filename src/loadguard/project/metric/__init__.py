#!/usr/bin/env python3
"""
# loadguard.project.metric

This file is a part of LoadGuard Runner.

(c) 2021, Deepnox SAS.

This module provides utilities for metrics.

"""

from loadguard.utils.rest import BaseRestClient


class BaseMetricsClient(BaseRestClient):

    def __init__(self, scheme, host, base_path):
        super().__init(scheme, host, base_path)
