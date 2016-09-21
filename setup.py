# -*- coding:utf-8 -*-
import codecs
import os
try:
    from setuptools import setup
except:
    from distutils.core import setup

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

NAME = "multi-thread-closing"

DESCRIPTION = "this is a test package for packing python liberaries tutorial."

LONG_DESCRIPTION = read("README.md")

KEYWORDS = "multi thread management"

AUTHOR = "cn"

AUTHOR_EMAIL = "308299269@qq.com"

URL = "https://www.github.com/ShichaoMa/MultiThreadClosing"

VERSION = "1.0.1"

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