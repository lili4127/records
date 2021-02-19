#!/usr/bin/env python

"""
Call `pip install -e .` to install package locally for testing.
"""

from setuptools import setup

# build command
setup(
    name="records",
    version="0.0.1",
    author="Lior Tal",
    author_email="ljt2136@columbia.edu",
    license="GPLv3",
    description="A package for getting records from gbif",
    classifiers=["Programming Language :: Python :: 3"],
    entry_points={
        "console_scripts": [
        "records = records.__main__:main",
        ]
        },
        )
