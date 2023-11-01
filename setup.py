#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-conversor",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_conversor"],
    install_requires=[
        # NB: Pin these to a more specific version for tap reliability
        "singer-python",
        "requests",
        "flake8",
        "parameterized",
        "singer-tools",
    ],
    entry_points="""
    [console_scripts]
    tap-conversor=tap_conversor:main
    """,
    packages=["tap_conversor"],
    package_data={"schemas": ["tap_conversor/schemas/*.json"]},
    include_package_data=True,
)
