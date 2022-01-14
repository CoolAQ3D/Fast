import os, shutil
from Fast.CLI.path.abs_path import find_absolute_path
from pathlib import Path

from Fast.CLI import add_help

def template(template_name, create_file_name):

  add_help(
    name = "template",
    description = "get template file quickly",
    usage = "fast template (template name)",
    subcommands = ["discord", "flask", "setup"]
  )

  get_file(create_file_name, template_name)



def get_file(create_file_name, template_name):
    if template_name in "discord":
      print('Downloading Discord Template')
      template_path = find_absolute_path('discord_template.py', first=True)
    elif template_name in "flask":
      print('Downloading Flask Template')
      template_path = find_absolute_path('flask_template.py', first=True) 
    elif template_name in "setup":
      print('Downloading Setup Template')
      template_path = find_absolute_path('setup_template.py', first=True) 

    copy_file(create_file_name, template_path)

def copy_file(filename, path):

    f = open(filename, "w")
    print(f'Creating file: {filename}')

    new_path = find_absolute_path(filename, first=True, start_location=os.getcwd())
    shutil.copyfile(path, new_path)

    print(f'Successfully created {filename}')