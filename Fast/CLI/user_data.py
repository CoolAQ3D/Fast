
#Custom User Data Reader

#from rich.console import Console
import os, json, shutil, time
from rich.progress import track
from rich.console import Console

from Fast.CLI.first_time_runner import FirstTimeScript

console = Console()
from Fast.CLI.path.abs_path import find_absolute_path

class UserData:
  def load():
    remove_hashtag = []
    data_only = []

    #Will make a folder to store datas
    fast_folder_path = FirstTimeScript.create_fast_info_folder()


    try:
        user_data =open(f"{fast_folder_path}Fast_Data.txt","r")
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
      UserData.create(fast_folder_path)
      settings = UserData.load()
      return settings
    except Exception as e:
      print(f"Error Settings Data: {e}")
  
  def create(fast_folder_path):
    try:
      #First Time run only such as creating data, loading bar
      FirstTimeScript.create_data()
      FirstTimeScript.loading_bar()
      FirstTimeScript.copy_readme()

      console.print("#2: Successfully setup FAST CLI.")
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



