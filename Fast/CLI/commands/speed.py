import os, speedtest
st = speedtest.Speedtest()

from rich.console import Console
from rich.table import Table
from Fast.CLI import add_help


console = Console()

def speed(
  cli=False
  ):

  add_help(
    name = "speed",
    description = "shows internet speed",
    usage = "fast speed (optional: cli)",
    subcommands = []
  )
  
  #Speedtest-cli version 
  if cli:
    os.system('speedtest-cli')
    return
  
  def convert_bytes(size):
      for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
          if size < 1024.0:
              return "%3.1f %s" % (size, x)
          size /= 1024.0   
      return size

  def generate_rich_table(download, upload):
    table = Table(show_header=True, header_style="bold red")
    table.add_column("Type", style="#8EEA18", width=12)
    table.add_column("Internet Speed")
    table.add_row(
      "Download", download
    )
    table.add_row(
      "Upload", upload
    )
    console.print(table)

  def get_download():
    download_speed = st.download()
    download_speed = convert_bytes(download_speed)
    return download_speed

  def get_upload():
    upload_speed = st.upload()
    upload_speed = convert_bytes(upload_speed)
    return upload_speed
  
  download = get_download()
  upload = get_upload()

  generate_rich_table(download, upload)

