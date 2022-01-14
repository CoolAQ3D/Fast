import json, speedtest

from Fast.CLI import add_help

from rich.console import Console
console = Console()
st = speedtest.Speedtest()



def wifi():
  
  add_help(
    name = "wifi",
    description = "shows wifi info",
    usage = "fast wifi",
    subcommands = []
  )

  console.print("Getting Internet/Wifi Information...", style="#24E883")
  internet_information = st.get_config()
  print(json.dumps(internet_information, indent=2))

