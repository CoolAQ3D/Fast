
#library usage

import os
from rich.console import Console
from rich.traceback import install

from Fast.Template.flask_template import start_server 

console = Console()

def start(
  #pass requirements path to automatically install
  requirements = None,
  rich_traceback = False,
  flask = False
):
  if requirements:
    console.print(f'Installing requirements from {requirements}')
    os.system(f'pip install -r {requirements}')
  
  if rich_traceback:
    console.print('Installing Rich Traceback')
    install()
  
  if flask:
    start_server()

    
