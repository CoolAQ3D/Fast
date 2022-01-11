
import os

def find_absolute_path(filename, first=False, start_location=None):

    if start_location:
      file_path = file_walk(filename, start_location)
      if file_path:
        if first:
          return file_path[0]
        else:
          return file_path
      else:
        return None

    #If in library, site packages
    library_path = '/opt/virtualenvs/python3/lib/python3.8/site-packages'

    #Look for home directory if can't find in library
    #Should return /home/runner/ filename
    home_path = os.getcwd()

    library = file_walk(filename, library_path)

    if library:
      if first:
        return library[0]
      else:
        return library
    else:
      home = file_walk(filename, home_path)
      if home:
        if first:
          return home[0]
        else:
          return home
      else:
        return None
    


def file_walk(filename, start_location):
  # Wlaking top-down from the root
  result = []
  for root, dir, files in os.walk(start_location):
    if filename in files:
      result.append(os.path.join(root, filename))
  
  return result