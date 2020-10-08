#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import setuptools


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


with open("requirements.txt", "r") as file_install:
    lines = file_install.readlines()
    install_requires = [x.strip("\n") for x in lines]

setuptools.setup(
    name='simple_report_cli',
    version='0.0.13',
    author='Maksim Grafskiy',
    author_email='maxograf@gmail.com',
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'simple_report_cli = simple_report_cli.cli:main']
    },
)
