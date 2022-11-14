#!/usr/bin/env python
import os
from setuptools import find_packages, setup

from mutant import __version__

MODULE_PATH = os.path.abspath(os.path.dirname(__file__))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mutant.settings")

setup(
    name='django-mutant',
    version=__version__,
    description='Dynamic model definition and alteration (evolving schemas)',
    long_description=open(os.path.join(MODULE_PATH, 'README.rst')).read(),
    url='https://github.com/charettes/django-mutant',
    author='Simon Charette',
    author_email='charette.s@gmail.com',
    install_requires=[
        'django>=3.0,<4.2',
        'django-picklefield>=0.3.2',
        'django-polymodels>=1.4.6a3',
        'six'
    ],
    packages=find_packages(exclude=['tests', 'tests.*']),
    package_data={
        '': ['locale/*/LC_MESSAGES/*'],
    },
    license='MIT License',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
