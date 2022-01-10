import os, sys, json
from rich.console import Console
from commands import Commands, Commands_Info

import inspect

console = Console()

def cli():
  
  arguments_length = len(sys.argv)
  arguments = sys.argv

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
  try:
    eval(f"Commands.{command}({subcommands})")
  except TypeError:
    #If invalid usage, show help
    Commands_Info.get(command)
  except AttributeError:
    console.print(f'This command is not found. \nType [#1CE27E]fast help[/#1CE27E]')


