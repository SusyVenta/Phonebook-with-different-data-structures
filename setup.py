# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


# with open('README.rst') as f:
#     readme = f.read()
#
# with open('LICENSE') as f:
#     license = f.read()

setup(
    name='Phonebook',
    version='1.0',
    description='Phonebook implementations with different data structures - python',
    # long_description=readme,
    author='Susanna Ventafridda',
    url='https://github.com/SusyVenta/Phonebook-with-different-data-structures',
    license=license,
    packages=find_packages(exclude=('tests',))
)
