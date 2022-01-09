import psutil, shutil, time, rich, os
import speedtest, json

from rich.console import Console

console = Console()

st = speedtest.Speedtest()

class Commands:
  def help():
 
    command_list = [command for command in dir(Commands) if command.startswith('__') is False]

    print("Available Commands \n" + ",".join(command_list))

  def speed():

    def convert_bytes(size):
      for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
          if size < 1024.0:
              return "%3.1f %s" % (size, x)
          size /= 1024.0
      
      return size

    console.print("Testing Download Speed...", style="#24E883")
    download_speed = st.download()
    print(f'Download Speed - {convert_bytes(download_speed)}')

    console.print("Testing Upload Speed...", style="#24E883")
    upload_speed = st.upload()
    print(f'Upload Speed - {convert_bytes(upload_speed)}')

  
  def speed_cli():
    os.system("speedtest-cli")
  
  def wifi():
    console.print("Getting Internet/Wifi Information...", style="#24E883")
    internet_information = st.get_config()
    print(json.dumps(internet_information, indent=2))
  
  def print(value):
    print("Printed - " + value)

  def ram():
    console.print('RAM memory % used:', psutil.virtual_memory()[2], style="bold green")
  
  def cpu():
    console.print('The CPU usage %: ', psutil.cpu_percent(1), style="bold green")
  
  def memory():
    total, used, free = shutil.disk_usage("/")
    print("Total: %d GB" % (total // (2**30)))
    print("Used: %d GB" % (used // (2**30)))
    print("Free: %d GB" % (free // (2**30)))
  

  #Search Specific File for it's location
  def path(filename, start_location = "/home/runner"):
    result = []

    # Wlaking top-down from the root
    for root, dir, files in os.walk(start_location):
      if filename in files:
         result.append(os.path.join(root, filename))
  
    if len(result) == 0:
      print("File not found! Probably doesn't exist!")
      return None
    else:
      print(result)
      return result
  
  def discord(create_file_name):
    print('Downloading Discord Template')

    search_location = "/opt/virtualenvs/python3/lib/python3.8/site-packages"

    path = Commands.path('discord_template.py', start_location=search_location)

    if path:
      HelperTools.copy_file(create_file_name, path)
    else:
      print('Searching in /home/runner dictionary')
      path = Commands.path("discord_template.py")

      if path:
        HelperTools.copy_file(create_file_name, path)
      else:
        return print("No file found in site-packages or home dictionary")
    
  
  
class HelperTools:
  def copy_file(filename, path):

    f = open(filename, "w")
    print(f'Creating file: {filename}')

    new_path = Commands.path(filename)
    shutil.copyfile(path[0], new_path[0])

    print(f'Successfully created {filename}')
