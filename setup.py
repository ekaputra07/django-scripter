#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "django-scripter",
    version = "0.1.0",
    url = 'https://github.com/ekaputra07/django-scripter',
	download_url = 'https://github.com/ekaputra07/django-scripter/downloads',
    license = 'BSD',
    description = "Scripts manager for Django.",
    author = 'Eka Putra',
    author_email = 'ekaputra@balitechy.com',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)

