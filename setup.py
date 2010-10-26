#!/usr/bin/env python
# -*- coding: utf8 -*-

from setuptools import setup, find_packages

setup(
    name = "wtf",
    version = "0.1",
    description = u"Post-mortem PDB handler",
    long_description = open('README', 'rb').read().decode('utf8'),
    url = u"http://github.com/k0001/wtf",
    author = u"Renzo Carbonara",
    author_email = u"gnuk0001@gmail.com",
    license = u"BSD",
    keywords = "pdb debug",
    zip_safe = True,
    packages = ['wtf'],
    include_package_data = True,
    classifiers = [
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Debuggers",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
    ]
)

