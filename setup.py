#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from codecs import open
from shutil import rmtree

from setuptools import find_packages, setup, Command

here = os.path.abspath(os.path.dirname(__file__))


class PublishCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except (OSError, IOError):
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        sys.exit()


class TestCommand(Command):
    description = 'Run Unit tests.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.status('Testing with pytest...')
        os.system('python -m pytest --cov=pk --cov-report term-missing tests -vv')


about = {}
with open(os.path.join(here, 'pk', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    keywords='dhis2',
    license='MIT',
    install_requires=[
        'requests>=2.4.2',
        'logzero>=1.3.1',
        'unicodecsv>=0.14.1',
        'six'
    ],
    entry_points={
        'console_scripts': [
            'dhis2-pk-indicator-definitions = pk.indicators:main',
            'dhis2-pk-share = pk.share:main',
            'dhis2-pk-userinfo = pk.userinfo:main',
            'dhis2-pk-post-css = pk.css:main'
        ]
    },
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    packages=find_packages(exclude=['tests']),
    test_suite='pytest',
    tests_require=['pytest'],
    setup_requires=['pytest-runner'],
    cmdclass={
        'publish': PublishCommand,
        'test': TestCommand
    },
)
