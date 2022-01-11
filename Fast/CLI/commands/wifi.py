import json, speedtest

from rich.console import Console
console = Console()
st = speedtest.Speedtest()

def wifi():
  console.print("Getting Internet/Wifi Information...", style="#24E883")
  internet_information = st.get_config()
  print(json.dumps(internet_information, indent=2))