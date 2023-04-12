from setuptools import find_packages, setup

VERSION = '1.0.1'

setup(
    name='django-mutant',
    version=VERSION,
    description='Dynamic model definition and alteration (evolving schemas)',
    long_description=open('README.rst').read(),
    url='https://github.com/charettes/django-mutant',
    author='Simon Charette',
    author_email='charette.s@gmail.com',
    install_requires=[
        'django>=3.0,<5.0',
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
