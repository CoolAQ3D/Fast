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


from rich.console import Console
console = Console()
console.print("Welcome to FastTools! \n type [bold #1CE27E]fast help[bold #1CE27E] to get started", style="bold red")