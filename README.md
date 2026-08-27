# Python Projects

[![tests](https://github.com/vladbrebe/python-projects/actions/workflows/tests.yml/badge.svg)](https://github.com/vladbrebe/python-projects/actions/workflows/tests.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A collection of small, self-contained Python programs covering object-oriented
design, data structures, recursion and input validation. This project
follows the freeCodeCamp "Python Certification" ciricullum. Every project runs
ona standard Python installation with no third-party dependencies, and every
project is covered by tests.

**Live overview:** <https://vladbrebe.github.io/python-projects/>

## Projects

| Project | What it demonstrates | Run it |
| --- | --- | --- |
| [Budget App](budget-app/) | Composition, operator overloading via `__str__`, text-mode charting | `python budget-app/budget.py` |
| [Email Client](email-client/) | Three-class domain model, exceptions over print statements | `python email-client/email_client.py` |
| [Hash Table](hash-table/) | Separate chaining, custom hash functions, Python's container protocols | `python hash-table/hash_table.py` |
| [ISBN Validator](isbn-validator/) | Check-digit arithmetic, defensive input handling | `python isbn-validator/isbn.py` |
| [Polygon Area Calculator](polygon-area-calculator/) | Inheritance and invariant-preserving setters | `python polygon-area-calculator/shapes.py` |
| [Tower of Hanoi](tower-of-hanoi/) | An iterative solution to a classically recursive puzzle | `python tower-of-hanoi/hanoi.py` |
| [User Settings](user-settings/) | Case-insensitive key handling, returning values rather than printing | `python user-settings/settings.py` |

## Getting started

```bash
git clone https://github.com/vladbrebe/python-projects.git
cd python-projects
python budget-app/budget.py
```

Python 3.10 or newer is required.

## Running the tests

The test suite uses [pytest](https://docs.pytest.org/) and covers all seven
projects.

```bash
python -m pip install pytest
pytest
```

Linting and formatting use [Ruff](https://docs.astral.sh/ruff/), configured in
`pyproject.toml`:

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
├── .github/workflows/tests.yml   Continuous integration
├── docs/index.html               Source of the GitHub Pages site
├── pyproject.toml                pytest and Ruff configuration
├── budget-app/
│   ├── README.md
│   ├── budget.py
│   └── test_budget.py
└── ...                           One folder per project, same shape
```
