from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='Exoplanet',
    version='1.0',
    test_suite='Test',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
)