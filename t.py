import os, sys
from rich.console import Console
from commands import Commands

console = Console()

def cli():
  
  arguments_length = len(sys.argv)
  arguments = sys.argv

  if arguments_length == 1:
    return print("Welcome to FastTools by MrCools!\nStart using by typing - fast help")
  #Up to 3 arguments supported as of now
  if arguments_length > 3:
    return print('Usage: fast command subcommand. \nMaybe you want to use quotes like "optional subcommands arguments" ? ')

  #SubCommand 
  try:
    command = arguments[1]
  except IndexError:
    return console.print('No commands provided')
  
  #Subcommand arguments
  try: 
    subcommand = arguments[2]
  except IndexError:
    subcommand = None


  try:
    if subcommand:
      #if subcommands takes arguments
      
      eval(f"Commands.{command + '(subcommand)'}")

    else:
      eval(f"Commands.{command}()")

  except AttributeError:
    return print('Unknown command, see available commands by typing fast help')
  except Exception as e:
    if "missing 1 required positional argument" in str(e):
      return print("This command needs subcommands")
    else:
      return print(e)




