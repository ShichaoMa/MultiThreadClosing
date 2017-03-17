# -*- coding:utf-8 -*-
try:
    from setuptools import setup
except:
    from distutils.core import setup

from multi_thread_closing import AUTHOR, AUTHOR_EMAIL, VERSION, URL

NAME = "multi-thread-closing"

DESCRIPTION = "Multi thread closing."

try:
    LONG_DESCRIPTION = open("README.rst").read()
except UnicodeDecodeError:
    LONG_DESCRIPTION = open("README.rst", encoding="utf-8").read()


KEYWORDS = "multi thread management"

LICENSE = "MIT"

setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords = KEYWORDS,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    license = LICENSE,
    py_modules = ["multi_thread_closing"],
    include_package_data=True,
    zip_safe=True,
)