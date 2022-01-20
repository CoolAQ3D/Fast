
#Update Help Commands Fast

import json
from Fast.CLI.path.abs_path import find_absolute_path


def add_help(
  name,
  description = "N/A",
  usage = "N/A",
  subcommands = [],
  alias = "N/A"
):
  help_path = find_absolute_path("fast-help.json", first=True)
    
  f = open(help_path)
  data = json.load(f)

  #If Exist, update
  try:
    data[name]
    data[name]['description'] = description
    data[name]['usage'] = usage
    data[name]['subcommands'] = subcommands
    data[name]['alias'] = alias
    

  #If doesn't exit, create
  except KeyError as e:
    #print(f"key - {e}")
    #print(f'Creating data for {name}')

    new_data = {
      f"{name}": {
        "description": f"{description}",
        "usage": f"{usage}",
        "subcommands": f"{subcommands}",
        "alias": f"{alias}"
      }
    }
    data.update(new_data)
  
  with open(help_path, 'w') as outfile:
      json.dump(data, outfile, indent=2)

