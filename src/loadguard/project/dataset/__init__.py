#!/usr/bin/env python3
"""
# loadguard.project.dataset

This file is a part of LoadGuard Runner.

(c) 2021, Deepnox SAS.

This module provides utilities to manage dataset.

"""

import csv
import os

CURRENT_PATH = os.path.dirname(__file__)
LG_HOME = os.path.abspath(os.path.join(CURRENT_PATH, '..', '..'))
LG_RESOURCES_DATASET_DIR = os.path.join(LG_HOME, 'resources', 'dataset')


class Dataset(object):
    rows = []

    def __init__(self, filename):
        self.filename = os.path.join(LG_RESOURCES_DATASET_DIR, filename)
        self.reader = csv.DictReader(open(self.filename), delimiter=';')
        self.load()

    def get(self, index):
        if index >= len(self.rows):
            return self.rows[(len(self.rows) - 1) % index]
        return self.rows[index]

    def load(self):
        [self.rows.append(row) for row in self.reader]
        return self
