# LoadGuard Runner

[![Tests](https://github.com/loadguard/runner/actions/workflows/tests.yml/badge.svg)](https://github.com/loadguard/runner/actions/workflows/tests.yml)
[![Build](https://github.com/loadguard/runner/actions/workflows/build.yml/badge.svg)](https://github.com/loadguard/runner/actions/workflows/build.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/80c0008dcf97f64e58c4/maintainability)](https://codeclimate.com/github/loadguard/runner/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/80c0008dcf97f64e58c4/test_coverage)](https://codeclimate.com/github/loadguard/runner/test_coverage)
[![License](https://img.shields.io/github/license/loadguard/runner.svg)](https://github.com/loadguard/runner/blob/main/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/loadguard/runner.svg)](https://github.com/loadguard/runner/graphs/contributors)
[![PyPI](https://img.shields.io/pypi/v/loadguard-runner.svg)](https://pypi.org/project/loadguard-runner/)
[![PyPI](https://img.shields.io/pypi/pyversions/loadguard-runner.svg)](https://pypi.org/project/loadguard-runner/)
<!--
[![codecov](https://codecov.io/gh/loadguard/runner/branch/devel/graph/badge.svg?token=IGALD1N09C)](https://codecov.io/gh/loadguard/runner)
-->

> An agnostic runner for automation of common tasks related to the performance test execution process.


## Table of Contents

* [Synopsis](#synopsis)
* [Usage](#usage)
* [Installation](#installation)
* [Build](#build)
* [Tests](#tests)
* [Développement](#develop)
* [Compatibility](#compatibility)
* [Issues](#issues)
* [Contributing](#contributing)
* [Credits](#credits)
* [Resources](#resources)
* [History](#history)
* [License](#license)

## <a name="synopsis">Synopsis</a>

LoadGuard is a SaaS agnostic solution for automating the process of preparing, executing, collecting and analyzing performance tests.

The LoadGuard Runner is an agnostic runner for automation of common tasks related to the performance test execution process..


## <a name="usage">Usage</a>

```python

```

## <a name="installation">Installation</a>

### Using `pip`

```bash
pip3 install loadguard-runner
```

### Using `setup.py`

Clone the repository:

```bash
git clone https://github.com/loadguard/runner
cd runner
git checkout main # or any branch, tag or commit...
```

Install dependencies:

```bash
python setup install

# or:
pip install -r requirements.txt
```

Optional, install dependencies to run unit tests:

```bash
pip install -r requirements-cicd.txt
```

## <a name="build">Build</a>

```bash
python3 setup.py build
```

## <a name="tests">Tests</a>

```bash
python3 setup.py test
```

### Code coverage

[Coverage.py](https://coverage.readthedocs.io/en/latest/) is required.

To run a code coverage process:

```bash
coverage run --omit '*/.venv/*' -m pytest test/ && coverage report -m
```

## Develop

Please install dependencies from files:

- `requirements.txt`
- `requirements-dev.txt`
- `requirements-cicd.txt`

Then install the [pre-commit](https://pre-commit.com/) hook to forbidden pushing code if unit tests are not passing.

## <a name="issues"> Issues</a>

Feel free to [submit issues](https://github.com/loadguard/runner/issues) and enhancement requests.

## <a name="contributing">Contributing</a>

Please refer to project's style guidelines and guidelines for submitting patches and additions. In general, we follow the "fork-and-pull" Git workflow.

1. **Fork** the repo on GitHub
2. **Clone** the project to your own machine
3. **Commit** changes to your own branch
4. **Push** your work back up to your fork
5. Submit a **Pull request** so that we can review your changes

**NOTE**: Be sure to merge the latest from "upstream" before making a pull request!

## <a name="credits">Credits</a>

Thank you very much to this used or integrated open source developments:

## <a name="resources">Resources</a>

Among others, to carry out this large and infinite project, we made use, among many others, of the following documentary resources.

Thank you to their authors for sharing their knowledge with our team.

## <a name="history">History</a>

Please refer to [the changelog file](CHANGELOG.md).

## <a name="license">License</a>

>
> [The MIT License](https://opensource.org/licenses/MIT)
>
> Copyright (c) 2021 [Deepnox SAS](https://deepnox.io/), Paris, France.
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
>AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.
>


