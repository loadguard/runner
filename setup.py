#!/usr/bin/env python3

"""
The setup script.

This file is a part of LoadGuard project.

(c) 2021, Deepnox SAS.

"""

import sys
from types import FunctionType
from distutils.core import Command

__name__ = "loadguard-runner"
""" The project name. """

__version__ = "0.0.5.2"
""" The current version (work in progress). """

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Cf. https://stackoverflow.com/a/23265673
try:
    from pypandoc import convert

    read_md: FunctionType = lambda f: convert(f, 'rst')
except ImportError:
    print("Warning: pypandoc module not found")
    read_md: FunctionType = lambda f: open(f, 'r').read()

with open("requirements.txt") as f:
    requires = f.readlines()
if sys.version_info[0] < 3 and sys.version_info[1] <= 6:
    raise Exception
else:
    tests_require = []
    test_command = [
        sys.executable,
        "-m",
        "pytest",
    ]  # Run unit tests
    coverage_command = [
        "coverage",
        "run",
        "-m",
        "pytest",
        "test/"
        "&&",
        "coverage",
        "report",
        "-m"
    ]  # Compute coverage
    coverage_xml = [
        "coverage",
        "xml",
    ]  # Export coverage as XML
    coverage_upload = [
        "codacy-coverage-reporter",
        "report",
    ]  # Upload to Codacity


class RunUnitTests(Command):
    """Run unit tests."""

    user_options = []
    description = __doc__[1:]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess

        errno = subprocess.call(test_command)
        raise SystemExit(errno)


class RunTestsCoverage(Command):
    """Run unit tests and report on code coverage using the 'coverage' tool."""

    user_options = []
    description = __doc__[1:]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess

        errno = subprocess.call(coverage_command)
        if errno == 0:
            subprocess.call(["coverage", "xml"])
        raise SystemExit(errno)


class UploadCoverage(Command):
    """Upload code coverage to Codacity."""

    user_options = []
    description = __doc__[1:]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess

        errno = subprocess.call(coverage_upload)
        if errno != 0:
            raise SystemExit(errno)


setup(
    name=__name__,
    version=f"{__version__}",
    description="An agnostic runner for automation of common tasks related to the performance test execution process.",
    license="Copyrighted 2021, Deepnox SAS",
    author="The Deepnox team",
    author_email="contact@deepnox.io",
    url="https://github.com/loadguard/runner",
    download_url=f"https://github.com/loadguard/runner/{__version__}.tar.gz",
    long_description=read_md("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Traffic Generation",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=[
        "deepnox",
        "load",
        "performance",
        "testing",
        "test"
    ],
    packages=[
        "loadguard",
        "loadguard.plugins",
        "loadguard.project",
        "loadguard.runner",
        "loadguard.scenarii",
        "loadguard.templates",
    ],
    package_dir={
        "loadguard": "src/loadguard",
        "loadguard.plugins": "src/loadguard/plugins",
        "loadguard.project": "src/loadguard/project",
        "loadguard.runner": "src/loadguard/runner",
        "loadguard.scenarii": "src/loadguard/scenarii",
        "loadguard.templates": "src/loadguard/templates",
    },
    scripts=[],
    install_requires=requires,
    tests_require=tests_require,
    cmdclass={
        "test": RunUnitTests,
        'coverage': RunTestsCoverage,
        # 'upload': UploadCoverage
    },
)
