from setuptools import setup, find_packages

setup(
    name='replikate',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'rpyc==5.3.1'
    ],
)