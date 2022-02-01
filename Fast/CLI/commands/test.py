from Fast.CLI import UserData
from rich.console import Console
console = Console()
#for testing purposes
import os, json


def test(_type=None):
  debug = UserData.settings.debug()
  if not debug:
    console.print("You need to enable debug/test mode for running this command...", style="red bold")
  elif _type=="data":
    user_data = UserData.load()
    print(json.dumps(user_data, indent=2))
  else:
    subcommands = _type
    TestCommmands.run(subcommands)
  

class TestCommmands:
  def run(subcommands):
    all_files = Browser.folder("/home")

    for x in all_files:
      print(x)
    
      

    
class Browser:
  def folder(start_location):
    all_files = []

    print(start_location)

    folder = [name for name in os.listdir(start_location) if os.path.isdir(name)]

    for n, each_folder in enumerate(folder):
      #folder[n] = f"📁 {each_folder}"
      all_files.append(f"{each_folder} 📁 ")
    
    file = [name for name in os.listdir(start_location) if os.path.isfile(name)]

    for n, each_file in enumerate(file):
      #file[n] = f"📁 {each_file}"
      all_files.append(f"{each_file} 📄 ")
    
    return all_files
    

  
  