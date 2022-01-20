import psutil, shutil
from rich.console import Console
from Fast.CLI import add_help

console = Console()

def system(system_type):

  add_help(
    name = "system",
    description = "shows various system info",
    usage = "fast system (type)",
    subcommands = ["memory", "cpu", "ram"],
    alias = "-sys"
  )

  if system_type in "ram":
    console.print('RAM memory % used:', psutil.virtual_memory()[2], style="bold green")
  
  elif system_type in "cpu":
    console.print('The CPU usage %: ', psutil.cpu_percent(1), style="bold green")
  
  elif system_type in "memory":
    total, used, free = shutil.disk_usage("/")
    print("Total: %d GB" % (total // (2**30)))
    print("Used: %d GB" % (used // (2**30)))
    print("Free: %d GB" % (free // (2**30)))