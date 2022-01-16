import json, speedtest

from Fast.CLI import add_help

from rich.console import Console
from rich.table import Table
console = Console()
st = speedtest.Speedtest()

import urllib.request


def wifi(all=False):
  
  add_help(
    name = "wifi",
    description = "shows wifi info",
    usage = "fast wifi",
    subcommands = []
  )

  #console.print("Getting Internet/Wifi Information...", style="#24E883")
  internet_information = st.get_config()

  if all == "all":
    print(json.dumps(internet_information, indent=2))
  else:
    ip = internet_information["client"]["ip"]
    isp  = internet_information["client"]["isp"]
    country = internet_information["client"]["country"]

    #Get More info by ip 
    with urllib.request.urlopen("https://geolocation-db.com/jsonp/"+ip) as url:data = url.read().decode()
    more_data = data.split("(")[1].strip(")")

    more_data = json.loads(more_data)
    generate_rich_table(ip, isp, country, more_data)


def generate_rich_table(ip, isp, country, more_data):
  table = Table(show_header=True, header_style="bold red")
  table.add_column("Type", style="#8EEA18", width=12)
  table.add_column("Wifi Information")
  table.add_row(
    "ISP", isp
  )
  table.add_row(
    "IP", ip
  )
  table.add_row(
    "State", more_data["state"]
  )
  table.add_row(
    "Country", country
  )

  console.print(table)
