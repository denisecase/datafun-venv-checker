"""
setup.py

This file configures the packaging for the Python project using setuptools.
It defines metadata, dependencies, and entry points for the package.

Functions:
- setup: Configures the package installation and distribution options.


"""

from setuptools import setup, find_packages

setup(
    name="datafun-venv-checker",
    version="0.1",
    description="A Python package to verify the existence and setup of a local project virtual environment (.venv)",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "check-venv=datafun_venv_checker.venv_checker:main",
        ],
    },
)
