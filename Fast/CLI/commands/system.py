import psutil, shutil
from rich.console import Console

console = Console()

def system(system_type):
  if system_type in "ram":
    console.print('RAM memory % used:', psutil.virtual_memory()[2], style="bold green")
  
  elif system_type in "cpu":
    console.print('The CPU usage %: ', psutil.cpu_percent(1), style="bold green")
  
  elif system_type in "memory":
    total, used, free = shutil.disk_usage("/")
    print("Total: %d GB" % (total // (2**30)))
    print("Used: %d GB" % (used // (2**30)))
    print("Free: %d GB" % (free // (2**30)))