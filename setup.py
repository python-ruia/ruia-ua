#!/usr/bin/env python
"""
 Created by howie.hu at 2018/9/22.
"""

import os

from setuptools import find_packages, setup


def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as f:
        return f.read()


setup(
    name='ruia_ua',
    version='0.0.1',
    author='Howie Hu',
    description="ruia_ua - simple user-agent middleware for Ruia.",
    long_description=read('README.md'),
    author_email='xiaozizayang@gmail.com',
    install_requires=['aiofiles', 'ruia>=0.0.1'],
    url="https://github.com/howie6879/ruia-ua/blob/master/README.md",
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    project_urls={
        'Documentation': 'https://github.com/howie6879/ruia-ua',
        'Source': 'https://github.com/howie6879/ruia-ua',
    },
    package_data={'ruia_ua': ['*.txt']},
)
