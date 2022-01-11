import psutil, shutil, time, rich, os
import speedtest, json

from rich.console import Console
from rich.tree import Tree
from Fast.file_viewer import walk_directory

from flask import Flask
from threading import Thread

console = Console()

st = speedtest.Speedtest()

class Commands:


  

  #Search Specific File for it's location

  
  def discord(create_file_name):
    print('Downloading Discord Template')

    start_location = "/opt/virtualenvs/python3/lib/python3.8/site-packages"

    path = Commands.path('discord_template.py', start_location=start_location)

    #using pip install git+location
    #should be working
    #using pip install -e . 
    #library will be in /home

    if path:
      HelperTools.copy_file(create_file_name, path)
    else:
      print('Searching in /home/runner dictionary')
      path = Commands.path("discord_template.py")

      if path:
        HelperTools.copy_file(create_file_name, path)
      else:
        return print("No file found in site-packages or home dictionary")
  
  def clear():
    cls = lambda: print("\033c\033[3J", end='')
    cls()
  
  def pycache():
    os.system("find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete")


  
  def print_json(filename):
    file_path = Commands.path(filename, start_location=".")
    f = open(file_path[0])
    data = json.load(f)
    print(json.dumps(data, indent=2))

 



    
class Commands_Info:
  def get(command):
    
    main_directory = "."
    library_directory = "/opt/virtualenvs/python3/lib/python3.8/site-packages"

    file_path = Commands.path("fast-help.json", start_location=library_directory, show_path=False)

    if file_path == None:
      file_path = Commands.path("fast-help.json", start_location=main_directory, show_path=False)

    f = open(file_path[0])
    data = json.load(f)
    
    invalid_usage = f'[red bold][Invalid Usage][/red bold]: [#1CE27E bold]{command}[/#1CE27E bold]'

    try:
      name = command
      description = data[command]['description']
      usage = data[command]['usage']
      subcommands = data[command]['subcommands']

      console.print(invalid_usage)
      console.print(f"[#F0CF3C bold][Description][/#F0CF3C bold]: {description}")
      console.print(f"[#F0CF3C bold][Usage][/#F0CF3C bold]: {usage}")

      if len(subcommands) != 0:
        console.print(f"[#F0CF3C bold][SubCommands][/#F0CF3C bold]: {subcommands}")

    except KeyError:
      console.print(invalid_usage)
      console.print(f"[red bold][Help][/red bold] not available for [#19EE69]{command}[/#19EE69]!")


class HelperTools:
  def copy_file(filename, path):

    f = open(filename, "w")
    print(f'Creating file: {filename}')

    new_path = Commands.path(filename)
    shutil.copyfile(path[0], new_path[0])

    print(f'Successfully created {filename}')
