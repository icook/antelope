#!/usr/bin/env python

from setuptools import setup, find_packages

requires = ['pymongo',
            'flask',
            'flask_mongoengine',
            'mongoengine',
            'flask-script',
            'yota']

setup(name='antelope',
      version='0.1',
      description='A simple finance management application',
      author='Isaac Cook',
      author_email='isaac@simpload.com',
      install_requires=requires,
      url='http://www.python.org/sigs/distutils-sig/',
      packages=find_packages('src'),
      package_dir={'': 'src'}
     )
