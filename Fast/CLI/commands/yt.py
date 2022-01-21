

from rich.console import Console

#Needed to Fix some lines of codes to start working pytube again, thats why pytube library won't work for now until its fixed and thats why needed to put the folder instead
from Fast.pytube import YouTube
console = Console()


from Fast.CLI import add_help

from Fast.CLI import UserData

import os


def yt(url):
  add_help(
    name = "ytdl",
    description = "YouTube Downloader",
    usage = "fast ytdl url (optional: custom or cc)"
  )
  download_video(url)



def download_video(url):

  settings = UserData.load()

  video_type = settings['video_type']
  video_quality = settings["video_quality"]
  
  try: 
    url = str(url)
    print(url)
    youtube = YouTube(url)
  except:
    return print('Invalid Video Link')
  
  if video_type == "mp4":
    print('running mp4')
    video = youtube.streams.filter(progressive=True, file_extension='mp4', res=video_quality).first()
  else:
    print('running mp3')
    #assume it's mp3
    video = youtube.streams.filter(only_audio=True).first()
  
  download_path = "./Downloads"
  if not os.path.isdir(download_path):
   os.makedirs(download_path)

  downloadFile = video.download(download_path)
  print(f'Downloading {url}')

  print(f'Video_Type: {video_type}')
  print(f'Video_Quality: {video_quality}')
  return print(downloadFile)
