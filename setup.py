import os
from setuptools import setup

def read_file(name):
    """
    Read file content
    """
    f = open(name)
    try:
        return f.read()
    except IOError:
        print("could not read %r" % name)
        f.close()

setup(
    name='basecrm',
    version='1.0.0',
    description='BaseCRM Official API V library client for Python',
    long_description=read_file('README.md'),
    author='BaseCRM developers',
    author_email='developers@getbase.com',
    url='https://github.com/basecrm/basecrm-python',
    license='MIT',
    packages=['basecrm', 'basecrm.test'],
    test_suite='basecrm.test.all',
    install_requires=['requests', 'bunch', 'six'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ])
