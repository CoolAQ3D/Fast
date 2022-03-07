
#git clone
#specific directory only

import os, shutil

from rich.console import Console
console = Console()
from Fast.CLI import add_help

def clone(url, folder_path, move_path):

  add_help(
    name = "clone",
    description = "clone github files (specific directory only)",
    usage = "fast clone url",
    subcommands = [],
  )

  os.system(f"git clone {url}")
  os.replace(folder_path, move_path)
  git_name = folder_path.split("/")[0]
  shutil.rmtree()

  