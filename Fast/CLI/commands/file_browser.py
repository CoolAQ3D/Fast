
#Browse File Real Time with Console/Terminal
from colorama import Fore, Back, Style
import os, inquirer, time
import timeout_decorator 
from rich.console import Console
from rich.syntax import Syntax
from rich.table import Table

console = Console()
def fb(path="/"):

  if path == "l":
    path = "/opt/virtualenvs/python3/lib/python3.8/site-packages"
  elif path == "h":
    path = "/home/runner/Fast-Studio-for-Testing"
    
  while True:
    #Clear Console for clean browsing 
    cls = lambda: print("\033c\033[3J", end='')
    cls()

    render_path_header = path
    
    #If only path is / says root directory isntead
    if len(render_path_header) == 1:
      render_path_header = "Root Directory"
    else:
      render_path_header = render_path_header[1:]

    table = Table(show_header=False, header_style="bold magenta")
    table.add_row(render_path_header)
    console.print(table)

    #try:
    value = File_Browser.start(path)
    #except TimeoutError:
    #Will Catch by debug
    # pass
    
    if value == "⭐ EXIT":
      break
    elif value == "⭐ BACK":
      path = path + "/"
      path = path.split("/")
      del path[-1]
      del path[-1]
      path = "/".join(path)
      print(path)
    elif value == "==========":
      pass
    else:
      if value.startswith("📙 "):
        value = value[2:]
      elif value.startswith("📝 "):
        value = value[2:]
      path = path + "/" + value
    

class File_Browser:
  @timeout_decorator.timeout(30)
  def start(path):
    
    is_file = os.path.isfile(path)
    if is_file:
      all_lines = []
      with open(path, 'r') as content:
        for line in content:
          all_lines.append(line)

      all_lines = "".join(all_lines)
      syntax = Syntax(all_lines, "python", theme="monokai", line_numbers=True)
      console.print(syntax)

    all_files = []

    for root, dirs, files in os.walk(path):

      copy_dirs = dirs
      copy_files = files
      
      #for n,x in enumerate(dirs):
      #  dirs[n] = x + "📁"

      all_files = dirs + files
      
      break

    all_files = sorted(all_files)

    #Place File Emoji
    for n,x in enumerate(all_files):
      for y in copy_dirs:
        if y == x:
          all_files[n] = "📙 " + all_files[n]
    
    #Place File Emoji
    for n,x in enumerate(all_files):
      for y in copy_files:
        if y == x:
          all_files[n] = "📝 " + all_files[n]

    all_files.insert(0,"==========")
    all_files.insert(0,'⭐ BACK')
    all_files.insert(0,'⭐ EXIT')
    #all_files.insert(0,"==========")

    questions = [
        inquirer.List(
            "value",
            message=Fore.RED + "File",
            choices=all_files,
        ),
    ]

    answers = inquirer.prompt(questions)
    value = answers["value"]

    return value
