import json
from rich.console import Console
console = Console()
from Fast.CLI.path.abs_path import find_absolute_path
def debug(value):
  data_path = find_absolute_path("config.json", first=True)
  f = open(data_path)
  data = json.load(f)

  if value in "true" or value in "on":
    #_debug = data['Fast']['Debug']
    #print(_debug)
    data['Fast']['Debug'] = "true"
    with open(data_path, 'w') as outfile:
      json.dump(data, outfile)
    
    console.print('[red bold][Debug][/red bold] Turned on debug mode!')
  elif value in "false" or value in "off":
    data['Fast']['Debug'] = "false"
    with open(data_path, 'w') as outfile:
      json.dump(data, outfile)
    
    console.print('[red bold][Debug][/red bold] Turned off debug mode!')
  else:
    console.print('[red bold][Debug][/red bold] Only true/on or false/off accepted')
  