# -*- coding: utf-8 -*-
"""Installer for the max5.client package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])

requires = [
    'requests'
]

wsgi_requires = ['max', 'WebTest']

setup(
    name='max5.client',
    version='0.1',
    description="Client library wrapper to access MAX API Plone %",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='Plone Team',
    author_email='plone.team@upcnet.es',
    url='https://pypi.python.org/pypi/max5.client',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['max5'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=requires,
    extras_require={
          'wsgi': requires + wsgi_requires
    },
    entry_points="""
    """,
)
