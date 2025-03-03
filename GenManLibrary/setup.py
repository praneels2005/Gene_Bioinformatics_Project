from setuptools import find_packages, setup

'''
In order to have it installed automatically only when you run tests you can add the following to your setup.py:

install_requires=[],
setup_requires=['pytest-runner'],
tests_require=['pytest==4.4.1'],
test_suite='tests',
'''

setup(
    name='GenManLib',
    packages=find_packages(include=['GenManLib']),
    version='0.1.0',
    description='A multitude of gene manipulation techniques',
    author='Praneel Pothukanuri',
)