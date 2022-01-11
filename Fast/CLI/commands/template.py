import os, shutil
from Fast.CLI.path.abs_path import find_absolute_path
from pathlib import Path

def template(template_name, create_file_name):
  if template_name in "discord":
    discord(create_file_name)



def discord(create_file_name):
    print('Downloading Discord Template')

    discord_template_path = find_absolute_path('discord_template.py', first=True)

    print(f'Discord Path = {discord_template_path}')

    copy_file(create_file_name, discord_template_path)

def copy_file(filename, path):

    f = open(filename, "w")
    print(f'Creating file: {filename}')

    new_path = find_absolute_path(filename, first=True, start_location=os.getcwd())
    print(f"File Area {new_path}")
    shutil.copyfile(path, new_path)

    print(f'Successfully created {filename}')