from setuptools import setup, find_packages

#More stuffs
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call

from Fast.CLI.user_data import UserData

#Create UserData File on install
UserData.create()
class PostInstallCommand(install):
  def run(self):
      install.run(self)
      print("hellllllllloooooo world")


setup(
  name="FastTools",
  version="1.0.0",
  author='MrCools',
  packages=find_packages(),
  install_requires=[
    'discord',
    'rich',
    'speedtest-cli',
    'psutil',
    "phonenumbers"
  ],
  include_package_data=True,
  package_data={'': ['*.json', "*.txt"]},
  #py_modules=['fast', 'commands', 'file_viewer'],
  entry_points='''
  [console_scripts]
  fast=Fast.CLI.fast:cli
  ''',
  cmdclass={
        'install': PostInstallCommand,
    },
)