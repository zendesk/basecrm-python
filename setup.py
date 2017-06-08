import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='basecrm',
    version='1.2.3',
    description='BaseCRM Official API V2 library client for Python',
    long_description=README,
    author='BaseCRM developers',
    author_email='developers@getbase.com',
    url='https://github.com/basecrm/basecrm-python',
    license='MIT',
    packages=['basecrm', 'basecrm.test'],
    test_suite='basecrm.test.all',
    install_requires=['requests', 'munch'],
    tests_require=['mock'],
    use_2to3=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ])
