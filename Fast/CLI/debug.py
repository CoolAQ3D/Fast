from Fast.CLI.path.abs_path import find_absolute_path

import json

#Enable Extra features if debug is on!
class Debug:
  def info():
  #Debug Mode
    data_path = find_absolute_path("config.json", first=True)
    f = open(data_path)
    data = json.load(f)
    debug = data['Fast']['Debug']
    if debug in "true":
      return True
    else:
      return False