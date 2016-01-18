#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


classifiers = """\
    Development Status :: 4 - Beta
    Operating System :: OS Independent
    Programming Language :: Python
    Programming Language :: Python :: 2
    Programming Language :: Python :: 2.7
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.3
    Programming Language :: Python :: 3.4
    Programming Language :: Python :: 3.5
"""


def _read(*parts, **kwargs):
    filepath = os.path.join(os.path.dirname(__file__), *parts)
    encoding = kwargs.pop('encoding', 'utf-8')
    with io.open(filepath, encoding=encoding) as fh:
        text = fh.read()
    return text


def get_version():
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        _read('cooler', '__init__.py'),
        re.MULTILINE).group(1)
    return version


def get_long_description():
    return _read('README.md')


install_requires = ['six', 'numpy', 'scipy', 'pandas', 'h5py']


setup(
    name='cooler',
    author='Nezar Abdennur',
    author_email='nezar@mit.edu',
    version=get_version(),
    license='BSD3',
    description='Sparse binary format for Hi-C genomic contact heatmaps',
    long_description=get_long_description(),
    keywords=['genomics'],
    url='https://github.com/mirnylab/cooler',
    packages=['cooler'],
    zip_safe=False,
    classifiers=[s.strip() for s in classifiers.split('\n') if s],
    install_requires=install_requires,
    tests_require=['nose'],
    extras_require={'docs': ['Sphinx>=1.1', 'numpydoc']},
)