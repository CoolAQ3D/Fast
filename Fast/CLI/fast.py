import os, sys, json
from rich.console import Console

from Fast.CLI.cli_handler import Command_Handler

console = Console()
#from rich.traceback import install
#install(show_locals=True)

def cli():
  
  arguments_length = len(sys.argv)
  arguments = sys.argv

  #If only type - Fast
  if arguments_length == 1:
    return print("Welcome to FastTools by MrCools!\nStart using by typing - fast help")

  #Remove fast from argument 
  arguments.pop(0)

  #Get Command Name
  command = arguments[0]

  #Remove Command, only keeps values or paraments 
  arguments.pop(0)

  subcommands = []
  for x in arguments:
    subcommands.append(f"'{x}'")
  
  subcommands = ",".join(subcommands)

  #Run Commands
  Command_Handler.run(command, subcommands)


