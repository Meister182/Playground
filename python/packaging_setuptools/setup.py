#! /usr/bin/env python3

import setuptools

setuptools.setup(
    name="my_py_pkg",
    version="0.1",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "my_py_pkg = my_py_pkg.__main__:main",
        ],
    },
    python_requires=">=3.6.2",
)
