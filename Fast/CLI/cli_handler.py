import time, os, json
from rich.console import Console
from pathlib import Path

from Fast.CLI.path.abs_path import find_absolute_path
from Fast.CLI.debug import Debug
from Fast.CLI import UserData

console = Console()


class Command_Handler:

  from Fast.CLI.commands.debug import debug
  from Fast.CLI.commands.print import print
  from Fast.CLI.commands.wifi import wifi
  from Fast.CLI.commands.speed import speed
  from Fast.CLI.commands.system import system
  from Fast.CLI.commands.file import file  
  from Fast.CLI.commands.tools import tools
  from Fast.CLI.commands.template import template
  from Fast.CLI.commands.phone_number import phone
  from Fast.CLI.commands.yt import yt

  #For testing add help
  from Fast.CLI.commands.test import test


  def run(command, subcommands):
  
    #For Run Speed
    start_time = time.time()
    #debug = Debug.info()
    debug = UserData.settings.debug()

    try:
      if command == "help":
        #for help
        command = subcommands
        Command_Handler.help(command)
      elif command == "run":
        #if try to use run function which is this
        #will ignore 
        raise AttributeError("Permission Deniend!")
      elif command == "-v":
        print("Version: 1.0.0")
      elif command[0] == "-":
        command = Alias.get(command)
        if command:
          eval(f"Command_Handler.{command}({subcommands})")
        else:
          print(f"Alias {subcommands} not found")
      else:
        eval(f"Command_Handler.{command}({subcommands})")

      end_time = time.time()
      if debug:
        console.print(f'[#8EEA18 bold][Speed][/#8EEA18 bold] Took [red bold]{round(end_time-start_time, 1)}s [/red bold] to run!')

    except TypeError as e:
      #If invalid command usages
      Commands_Info.get(command)
      if debug:
        console.print(f'[red bold][Debug][/red bold] {e}')
    except AttributeError as e:
      #If commands not found
      console.print(f'This command is not found. \nType [#1CE27E]fast help[/#1CE27E]')
      if debug:
        console.print(f'[red bold][Debug][/red bold] {e}')
    except Exception as other_erros:
      if debug:
        console.print(f"[red bold][Debug][/red bold] {other_erros}")

    
  def help(command_name=None):
    
    #If given command run, show that command help instead of all
    if command_name:

      Commands_Info.get(command_name[1:-1])
      return
 
    command_list = [command for command in dir(Command_Handler) if command.startswith('__') is False]

    console.print("[bold #1CE27E]Available Commands[/bold #1CE27E] \n" + ",".join(command_list))

 ##Alias Feature fast -a help   
class Alias:
  def get(command):
    help_path = find_absolute_path("fast-help.json", first=True)
    
    f = open(help_path)
    data = json.load(f)

    for command_name in data:
      try: 
        alias = data[command_name]['alias']
        if alias == command:
          #print(command_name)
          return command_name
      except:
        return None



class Commands_Info:
  def get(command):
    
    help_path = find_absolute_path("fast-help.json", first=True)
    
    f = open(help_path)
    data = json.load(f)

    print(command)

    
    invalid_usage = f'[red bold][Invalid Usage][/red bold]: [#1CE27E bold]{command}[/#1CE27E bold]'

    try:
      name = command
      description = data[command]['description']
      usage = data[command]['usage']
      subcommands = data[command]['subcommands']
      alias = data[command]['alias']

      console.print(invalid_usage)
      console.print(f"[#F0CF3C bold][Description][/#F0CF3C bold]: {description}")
      console.print(f"[#F0CF3C bold][Usage][/#F0CF3C bold]: {usage}")

      if len(subcommands) != 0:
        console.print(f"[#F0CF3C bold][SubCommands][/#F0CF3C bold]: {subcommands}")
      
      if alias != "N/A":
        console.print(f"[#F0CF3C bold][Alias][/#F0CF3C bold]: {alias}")


    except KeyError as e: 
      console.print(invalid_usage)
      console.print(f"[red bold][Help][/red bold] not available for [#19EE69]{command}[/#19EE69]!")
