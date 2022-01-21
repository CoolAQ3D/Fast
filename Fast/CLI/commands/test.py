from Fast.CLI import UserData
#for testing purposes

import json
def test():
  settings = UserData.load()
  #settings = json.loads(settings)
  print(json.dumps(settings, indent=2))

