import time, os, json
from rich.console import Console

console = Console()

debug_mode = True

class Command_Handler:

  from Fast.CLI.commands.print import print
  from Fast.CLI.commands.wifi import wifi
  from Fast.CLI.commands.speed import speed
  from Fast.CLI.commands.system import system
  from Fast.CLI.commands.file import file


  def run(command, subcommands):
  
    #For Run Speed
    start_time = time.time()

    try:
      if command == "help":
        Command_Handler.help(subcommands)
      elif command == "run":
        #if try to use run function which is this
        #will ignore 
        raise AttributeError
      else:
        eval(f"Command_Handler.{command}({subcommands})")

      end_time = time.time()
      if debug_mode:
        console.print(f'[#8EEA18 bold][Speed][/#8EEA18 bold] Took {round(end_time-start_time, 1)}s to run!')

    except TypeError:
      #If invalid command usages
      Commands_Info.get(command)
    except AttributeError:
      #If commands not found
      console.print(f'This command is not found. \nType [#1CE27E]fast help[/#1CE27E]')
    
  def help(command_name=None):
    
    #If given command run, show that command help instead of all
    if command_name:
      Commands_Info.get(command_name)
      return
 
    command_list = [command for command in dir(Command_Handler) if command.startswith('__') is False]

    console.print("[bold #1CE27E]Available Commands[/bold #1CE27E] \n" + ",".join(command_list))
    



class Commands_Info:
  def get(command):
    
    current_directory = os.getcwd()

    help_path = f"{current_directory}/Fast/CLI/fast-help.json"

    f = open(help_path)
    data = json.load(f)

    print(command)

    
    invalid_usage = f'[red bold][Invalid Usage][/red bold]: [#1CE27E bold]{command}[/#1CE27E bold]'

    try:
      name = command
      description = data[command]['description']
      usage = data[command]['usage']
      subcommands = data[command]['subcommands']

      console.print(invalid_usage)
      console.print(f"[#F0CF3C bold][Description][/#F0CF3C bold]: {description}")
      console.print(f"[#F0CF3C bold][Usage][/#F0CF3C bold]: {usage}")

      if len(subcommands) != 0:
        console.print(f"[#F0CF3C bold][SubCommands][/#F0CF3C bold]: {subcommands}")

    except KeyError: 
      console.print(invalid_usage)
      console.print(f"[red bold][Help][/red bold] not available for [#19EE69]{command}[/#19EE69]!")
