
from setuptools import setup, find_packages

setup(
  name="Package Name",
  version="1.0.0",
  author='MrCools',
  packages=find_packages(),
  install_requires=[],
  include_package_data=True,
  package_data={'': ['*.json']},
  py_modules=[],
  entry_points='''
  [console_scripts]
  prefix=function_file_path:function_name
  '''
)
