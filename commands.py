import psutil, shutil, time, rich, os
import speedtest, json

from rich.console import Console
from rich.tree import Tree
from file_viewer import walk_directory

from flask import Flask
from threading import Thread

console = Console()

st = speedtest.Speedtest()

class Commands:
  def help(command_name=None):
    
    #If given command run, show that command help instead of all
    if command_name:
      Commands_Info.get(command_name)
      return
 
    command_list = [command for command in dir(Commands) if command.startswith('__') is False]

    console.print("[bold #1CE27E]Available Commands[/bold #1CE27E] \n" + ",".join(command_list))

  def speed():
    def convert_bytes(size):
      for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
          if size < 1024.0:
              return "%3.1f %s" % (size, x)
          size /= 1024.0   
      return size

    console.print("Testing Download Speed...", style="#24E883")
    download_speed = st.download()
    print(f'Download Speed - {convert_bytes(download_speed)}')

    console.print("Testing Upload Speed...", style="#24E883")
    upload_speed = st.upload()
    print(f'Upload Speed - {convert_bytes(upload_speed)}')

  
  def speed_cli():
    os.system("speedtest-cli")
  
  def wifi():
    console.print("Getting Internet/Wifi Information...", style="#24E883")
    internet_information = st.get_config()
    print(json.dumps(internet_information, indent=2))
  
  def print(value):
    print("Printed - " + value)

  def ram():
    console.print('RAM memory % used:', psutil.virtual_memory()[2], style="bold green")
  
  def cpu():
    console.print('The CPU usage %: ', psutil.cpu_percent(1), style="bold green")
  
  def memory():
    total, used, free = shutil.disk_usage("/")
    print("Total: %d GB" % (total // (2**30)))
    print("Used: %d GB" % (used // (2**30)))
    print("Free: %d GB" % (free // (2**30)))
  

  #Search Specific File for it's location
  def path(filename, start_location = "/home/runner", show_path=True):
    result = []

    # Wlaking top-down from the root
    for root, dir, files in os.walk(start_location):
      if filename in files:
         result.append(os.path.join(root, filename))
  
    if len(result) == 0:
      print("File not found! Probably doesn't exist!")
      return None
    else:
      if show_path:
        print(result)
      return result
  
  def path_lib(filename):
    start_location = "/opt/virtualenvs/python3/lib/python3.8/site-packages"
    Commands.path(filename, start_location=start_location)
  
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

  #Makes file
  def file(filename):
    open(filename, "w")
    print(f'Created {filename}')
  
  def print_json(filename):
    file_path = Commands.path(filename, start_location=".")
    f = open(file_path[0])
    data = json.load(f)
    print(json.dumps(data, indent=2))

  def test(x,y,z, lol=None):
    print(x)
    print(y)
    print(z)
    print(lol)
  
  def fish(bird, animal, whatever, sky, earth, universe):
    pass
  
  def file_view(path):
    tree = Tree(
        f"Main File Area - {os.getcwd()}",
        guide_style="bold bright_blue",
    )
    walk_directory(path, tree)
    console.print(tree)
  



    
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
