#!/usr/bin/python

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='ipynb_format',
      version='0.1.0',
      description='A code formatter for python code in ipython notebooks',
      long_description=long_description,
      url='https://github.com/fg1/ipynb_format',
      author='fg1',
      license='BSD',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
      ],
      keywords='ipython notebook',
      packages=find_packages(),
      install_requires=['yapf'],
      entry_points={
          'console_scripts': [
              'ipynb_format=ipynb_format:cli',
          ],
      }, )