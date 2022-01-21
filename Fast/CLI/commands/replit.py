
#Get Info About Replit and Filesize, etc.
import os, sys
def replit():
  #Will get filename almost
  #using os.getcwd() 
  #breackets, etc. not supported

  replit_file_name = os.getcwd()
  replit_file_name = replit_file_name.split("/")
  replit_file_name = replit_file_name[3]

  size = 0
 
  # assign folder path
  Folderpath = os.getcwd()
  
  # get size
  for path, dirs, files in os.walk(Folderpath):
      for f in files:
          fp = os.path.join(path, f)
          size += os.path.getsize(fp)
  
  # display size
  #print("File Name is not 100% accurate since there is probably no way to get it currently")
  print(f'Replit File: {replit_file_name}')
  size = convert_bytes(size)
  print("File size: " + size)

  os.system("python --version")
  #os.system("node -v")
  #os.system("$BASH_VERSION")

  

def convert_bytes(size):
      for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
          if size < 1024.0:
              return "%3.1f %s" % (size, x)
          size /= 1024.0   
      return size