from Fast.CLI import UserData
from rich.console import Console
console = Console()
#for testing purposes
import os, json


def test(_type=None):
  debug = UserData.settings.debug()
  if not debug:
    console.print("You need to enable debug/test mode for running this command...", style="red bold")
  elif _type=="data":
    user_data = UserData.load()
    print(json.dumps(user_data, indent=2))
  else:
    TestCommmands.run()
  

class TestCommmands:
  def run():
    def underline(text):
      underline_text = '\u2500' * os.get_terminal_size().columns      
      
      underline_text_array = []

      for i in underline_text:
        underline_text_array.append(i)

      length = len(underline_text_array) / 2
      length = int(round(length, 0))

      n_times = 0

      text_size = len(text) / 2
      text_size = int(round(text_size, 0)) + 1

      for x in text:
        n_times += 1
        underline_text_array[length - text_size + n_times] = x
      
      #print(length)
       
      #print(underline_text_array)
      return "".join(underline_text_array)


    #console.print(underline("Fast CLI"), style="blue")
    #underline()
    pass