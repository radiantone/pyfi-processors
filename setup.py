#!/usr/bin/env python3

import os
import glob
import shutil
from setuptools import setup, Command
import distutils.cmd
import distutils.log
import setuptools
import subprocess

# get key package details from py_pkg/__version__.py
about = {}  # type: ignore
here = os.path.abspath(os.path.dirname(__file__))


# package configuration - for reference see:
# https://setuptools.readthedocs.io/en/latest/setuptools.html#id9
setup(
    name='ext processor',
    description='Example processors',
    long_description='',
    long_description_content_type='text/markdown',
    version='0.1',
    author='Darren Govoni',
    author_email='darren@ontrenet.com',
    url='https://github.com/radiantone/pyfi-processor',
    packages=['ext.processors'],
    include_package_data=True,
    python_requires=">=3.8.*",
    install_requires=[
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='parallel processing, devops, dataflow, supercomputing, workflows'
)
