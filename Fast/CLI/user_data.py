
#Custom User Data Reader

#from rich.console import Console
import os, json, shutil
#console = Console()
from Fast.CLI.path.abs_path import find_absolute_path

class UserData:
  def load():
    remove_hashtag = []
    data_only = []

    try:
        user_data =open("fast_data.txt","r")
        lines = user_data.read().split('\n')

        #remove lines that starts with #
        for line in lines:
          if not(line.startswith("#")): 
            remove_hashtag.append(line)
        
        #next remove empty lines ""
        for line in remove_hashtag:
          if len(line) != 0:
            data_only.append(line)


        
        #Supported Settings
        settings = {
          "debug": "",
          "video_type": "",
          "video_quality": "",
          "download_location": ""
        }


        #Update Data
        for each_data in data_only:
          each_settings = each_data.split("=")

          try:
            setting_name = each_settings[0].lower()
            setting_value = each_settings[1].lower()

            if setting_name in settings:
              settings[setting_name] = setting_value
          except KeyError:
            pass
        
        return settings
    except FileNotFoundError:
      UserData.create()
      settings = UserData.load()
      return settings
    except Exception as e:
      print(f"Error Settings Data: {e}")
  
  def create():
    try:
      path = find_absolute_path('fast_data_template.txt', first=True)

      filename = "fast_data.txt"

      f = open(filename, "w")
      print(f'Creating fast_data.txt')

      new_path = find_absolute_path(filename, first=True, start_location=os.getcwd())
      shutil.copyfile(path, new_path)

      print(f'Successfully created {filename}')
    except Exception as e:
      pass


  #Helper Commands
  #Quickly Acess to supported command such as debug 
  class settings:
    def debug():
      Settings = UserData.load()
      debug = Settings["debug"]

      if debug.lower() == "true" or debug.lower() == "on":
        return True
      else:
        return False



