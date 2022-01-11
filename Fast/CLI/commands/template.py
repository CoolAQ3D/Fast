import os, shutil
from Fast.CLI.commands.file import file

def template(template_name, create_file_name):
  if template_name in "discord":
    discord(create_file_name)



def discord(create_file_name):
    print('Downloading Discord Template')

    discord_template_path = file("path", "discord_template.py", start_location="library")

    copy_file(create_file_name, discord_template_path)

def copy_file(filename, path):

    f = open(filename, "w")
    print(f'Creating file: {filename}')

    new_path = file("path", filename, start_location="home")
    shutil.copyfile(path[0], new_path[0])

    print(f'Successfully created {filename}')