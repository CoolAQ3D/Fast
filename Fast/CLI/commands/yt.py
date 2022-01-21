

#Needed to Fix some lines of codes to start working pytube again, thats why pytube library won't work for now until its fixed and thats why needed to put the folder instead
from Fast.pytube import YouTube


from rich.console import Console
from rich.table import Table
console = Console()


from Fast.CLI import add_help

from Fast.CLI import UserData

import os


def yt(url):
  add_help(
    name = "yt",
    description = "YouTube Downloader",
    usage = "fast ytdl link or test (for sample)"
  )
  download_video(url)



def download_video(url):
  if url == "test":
    url = "https://www.youtube.com/watch?v=DAjMZ6fCPOo"

  settings = UserData.load()

  video_type = settings['video_type']
  video_quality = settings["video_quality"]
  download_location = settings["download_location"]
  
  try: 
    url = str(url)
    #print(url)
    youtube = YouTube(url)
  except:
    return print('Invalid Video Link')
  
  if video_type == "mp4":
    #print('running mp4')
    video = youtube.streams.filter(progressive=True, file_extension='mp4', res=video_quality).first()
  else:
    #print('running mp3')
    #assume it's mp3
    
    video = youtube.streams.filter(only_audio=True).first()
  
  downloadFile = video.download(f"./{download_location}")
  
  
  video_name = youtube.title
  video_size = convert_bytes(video.filesize)
   
  generate_rich_table(url, video_name, video_size, video_type, video_quality, download_location)


def generate_rich_table(url, video_name, video_size, video_type, video_quality, download_location):
  table = Table(show_header=True, header_style="bold red")
  table.add_column("Category", style="#8EEA18", width=12)
  table.add_column("YouTube Video Information", width=50)
  table.add_row(
    "Name", video_name
  )
  table.add_row(
    "Size", video_size
  )
  table.add_row(
    "Type", video_type
  )
  table.add_row(
    "Quality", video_quality
  )
  table.add_row(
    "Location", f"./{download_location}"
  )
  table.add_row(
    "URL", url
  )

  console.print(table)

def convert_bytes(size):
      for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
          if size < 1024.0:
              return "%3.1f %s" % (size, x)
          size /= 1024.0   
      return size