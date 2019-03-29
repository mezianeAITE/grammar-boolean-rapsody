#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Definition of setup function for setuptools module."""

# Standard imports
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

################################################################################

class PyTest(TestCommand):
    """Call tests with the custom 'python setup.py test' command."""

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        import pytest
        errno = pytest.main()
        sys.exit(errno)

################################################################################
 
setup(
 
    name='gbr',
    version="1.1",
 
    packages=find_packages(),
 
    author="Lucas Bourneuf",
 
    description="Using grammar, FSM, syntactic tree and DAG for answer to a simple question. There is better ways ; one of them is to code it in lisp.",
 
    long_description=open('README.md', encoding='utf8').read(),
 

    include_package_data=True,
 
 
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
    ],
)