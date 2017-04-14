#!/usr/bin/env python
# pylint: disable=missing-docstring
from setuptools import setup
setup(
    setup_requires=[
        'pbr>=2.1.0',
        'setuptools>=30.0'
    ],
    pbr=True,
    use_2to3=True,
    test_suite='basecrm.test.all',
)
