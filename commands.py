import os

class SubCommands:
  def sublist():
    subcommands_list = ['sublist', 'speed', 'print']
    print(subcommands_list)

  def speed():
    os.system('speedtest-cli')
  
  def print(value):
    print("Printed - " + value)
  
  def hah(x):
    print(x)
