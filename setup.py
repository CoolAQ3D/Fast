from setuptools import setup, find_packages

setup(
  name="FastTools v1",
  version="1.0.0",
  author='MrCools',
  packages=find_packages(),
  install_requires=[
    'discord',
    'rich'
  ],
  include_package_data=True,
  package_data={'': []},
  entry_points='''
  [console_scripts]
  fast=fasttools:cli
  '''
)