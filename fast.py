import os, sys
from rich.console import Console
from commands import SubCommands

console = Console()

def cli():
  
  arguments_length = len(sys.argv)
  arguments = sys.argv

  #Up to 3 arguments supported as of now
  if arguments_length > 3:
    return print('Usage: fast subcommand optional_arguments. \nMaybe you want to use quotes like "optional argumenents" ? ')

  #SubCommand 
  try:
    subcommand = arguments[1]
  except IndexError:
    return console.print('No subcommands provided')
  
  #Subcommand arguments
  try: 
    subcommand_arguments = arguments[2]
  except IndexError:
    subcommand_arguments = None


  try:
    if subcommand_arguments:
      #if subcommands takes arguments
      
      eval(f"SubCommands.{subcommand + '(subcommand_arguments)'}")

    else:
      eval(f"SubCommands.{subcommand}()")

  except AttributeError:
    return print('Unknown subcommand, see available subcommands by typing fast sublist')
  except Exception as e:
    if "missing 1 required positional argument" in str(e):
      return print("This command needs sub arguments")
    else:
      return print(e)




