# Python Projects

[![tests](https://github.com/vladbrebe/python-projects/actions/workflows/tests.yml/badge.svg)](https://github.com/vladbrebe/python-projects/actions/workflows/tests.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A collection of small, self-contained Python programs covering object-oriented
design, data structures, recursion and input validation. This project
follows the freeCodeCamp "Python Certification" curriculum. Every project runs
on a standard Python installation with no third-party dependencies, and every
project is covered by tests.

## Projects

| Project | What it demonstrates | Run it |
| --- | --- | --- |
| [Budget App](budget-app/) | Classes and Objects | `python budget-app/budget.py` |
| [Email Client](email-client/) | Classes and Objects | `python email-client/email_client.py` |
| [Hash Table](hash-table/) | Linear Data Structures | `python hash-table/hash_table.py` |
| [ISBN Validator](isbn-validator/) | Error handling | `python isbn-validator/isbn.py` |
| [Polygon Area Calculator](polygon-area-calculator/) | Object-Orientated Programming | `python polygon-area-calculator/shapes.py` |
| [Tower of Hanoi](tower-of-hanoi/) | Algorithms | `python tower-of-hanoi/hanoi.py` |
| [User Settings](user-settings/) | Dictionaries and Sets | `python user-settings/settings.py` |

## Getting started

```bash
git clone https://github.com/vladbrebe/python-projects.git
cd python-projects
python budget-app/budget.py
```

Made for Python 3.10 or newer

## Running the tests

The test suite uses [pytest](https://docs.pytest.org/) and covers all seven
projects.

```bash
python -m pip install pytest
pytest
```

```bash
python -m pip install ruff
ruff check .
ruff format --check .
```

Both run automatically on every push through GitHub Actions
(`.github/workflows/tests.yml`), against Python 3.10, 3.11 and 3.12.

## Repository layout

```
python-projects/
├── .github/workflows/tests.yml   
├── pyproject.toml                pytest and Ruff configuration
├── budget-app/
│   ├── README.md
│   ├── budget.py
│   └── test_budget.py
└── ...                           One folder per project, same shape
```
