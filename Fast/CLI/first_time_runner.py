
#Run Once after installing
#Checks if user_data exist, if not run once!

import time, shutil, os, requests
from rich.console import Console
from rich.progress import track
console = Console()

from Fast.CLI.path.abs_path import find_absolute_path

class FirstTimeScript:
  def create_data():
    r = requests.get("https://raw.githubusercontent.com/CoolAQ3D/Fast/main/Fast/Template/fast_data_template.txt")
    file_content = r.text

    fast_folder_path = FirstTimeScript.create_fast_info_folder()

    with open(f"{fast_folder_path}Fast_Data.txt", "w") as f: 
      f.write(file_content)

  def create_fast_info_folder():
    directory = "Fast Info"
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, directory)
    try:
      os.mkdir(path)
      #print("Directory '% s' created" % directory)
      return f"{directory}/"
    except FileExistsError:
      return f"{directory}/"

  def copy_readme():
    r = requests.get("https://raw.githubusercontent.com/CoolAQ3D/Fast/main/README.md")
    file_content = r.text

    fast_folder_path = FirstTimeScript.create_fast_info_folder()

    with open(f"{fast_folder_path}Fast_README.md", "w") as f: 
      f.write(file_content)
    
  def loading_bar():
    print("#1: Setting Up FAST CLI... \n-- First time, only!")
    for loading_bar in track(range(3), description="Fast CLI: \n"):
      time.sleep(1)
    