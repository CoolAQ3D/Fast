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
    'psutil'
  ],
  include_package_data=True,
  package_data={'': ['*.json']},
  #py_modules=['fast', 'commands', 'file_viewer'],
  entry_points='''
  [console_scripts]
  fast=Fast.CLI.fast:cli
  '''
)

print("Welcome to FastTools by MrCools!")