#from Fast.CLI.help.add_help import add_help
#Testing Command
from Fast.CLI import add_help

def test():
  #print("hi")
  #return
  #---Help---
  add_help(
  name = "test test test",
  description = "test ah",
  usage = "fast test",
  subcommands = []
  )