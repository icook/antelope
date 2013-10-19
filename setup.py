#!/usr/bin/env python

from setuptools import setup, find_packages

requires = ['pymongo',
            'flask',
            'flask_mongoengine',
            'mongoengine',
            'flask-script',
            'yota>=0.3']

setup(name='antelope',
      version='0.1',
      description='A simple finance management application',
      author='Isaac Cook',
      author_email='isaac@simpload.com',
      install_requires=requires,
      url='http://www.python.org/sigs/distutils-sig/',
      dependency_links=["https://github.com/icook/yota/tarball/0.3#egg=yota-0.3"],
      packages=find_packages('src'),
      package_dir={'': 'src'}
     )
