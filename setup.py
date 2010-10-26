#!/usr/bin/env python
# -*- coding: utf8 -*-

from setuptools import setup, find_packages

setup(
    name = "wtf",
    version = "0.2-dev",
    description = "Post-mortem PDB handler",
    long_description = open('README', 'rb').read().decode('utf8'),
    url = "http://github.com/k0001/wtf",
    author = "Renzo Carbonara",
    author_email = "gnuk0001@gmail.com",
    license = "BSD",
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

