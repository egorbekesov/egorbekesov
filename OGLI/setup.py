from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='OGLI',
    version='1.0',
    test_suite='Test',
    py_modules = ["OGlI"],
    install_requires=['requests', 'bs4', 'lxml', 'numpy'],
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
)