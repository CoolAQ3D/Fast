import os, sys
from rich.console import Console
from commands import Commands

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

  #print(f"Command Name: {command} \nSub Commands: {subcommands}")
  
  #Run Commands
  try:
    eval(f"Commands.{command}({subcommands})")
  except TypeError:
    err = eval(f"inspect.getargspec(Commands.{command})")
    err = str(err)
    #print(err)

    head, sep, tail = err.partition(', varargs')
    err = head
    
    err = err.replace('ArgSpec(args=', "")
    print(f"Required Subcommand: {err}")
  except AttributeError:
    print(f'Command {command} not found. \nType fast help')


    



