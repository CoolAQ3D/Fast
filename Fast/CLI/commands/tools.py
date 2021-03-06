import os, json
from rich.traceback import install
from Fast.CLI.commands.file import file
from Fast.CLI import add_help
from pathlib import Path



def tools(value, json_filename=None):

  add_help(
    name = "tools",
    description = "run quick tools",
    usage = "fast tools (subcommands)",
    subcommands = ["clear", "pycache", "pjson"]
  )

  if value in "clear":
    cls = lambda: print("\033c\033[3J", end='')
    cls()
  elif value in "pycache":
    os.system("find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete")
  elif value in "traceback":
    print("Installed Rich Traceback")
    install()
  elif value in "pjson":
    #should only reads json file from home directory 
    file_path = file("path", json_filename, start_location=".")
    f = open(file_path[0])
    data = json.load(f)
    print(json.dumps(data, indent=2))

    