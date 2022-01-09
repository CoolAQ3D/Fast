from setuptools import setup, find_packages

setup(
  name="FastTools",
  version="1.0.0",
  author='MrCools',
  packages=find_packages(),
  install_requires=[
    'discord',
    'rich',
    'speedtest-cli',
    'click',
    'psutil'
  ],
  include_package_data=True,
  package_data={'': []},
  py_modules=['fast', 'commands'],
  entry_points='''
  [console_scripts]
  fast=fast:cli
  '''
)