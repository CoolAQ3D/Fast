
#Things Needed to run fast library will put here

import os, requests


class Scripts:
  def underline(text):
        underline_text = '\u2500' * os.get_terminal_size().columns      
        
        underline_text_array = []

        for i in underline_text:
          underline_text_array.append(i)

        length = len(underline_text_array) / 2
        length = int(round(length, 0))

        n_times = 0

        text_size = len(text) / 2
        text_size = int(round(text_size, 0)) + 1

        for x in text:
          n_times += 1
          underline_text_array[length - text_size + n_times] = x
        
        #print(length)
        
        #print(underline_text_array)
        return "".join(underline_text_array)
  
   def download_changelog():
    r = requests.get("https://raw.githubusercontent.com/CoolAQ3D/Fast/main/Changelog.md")
    file_content = r.text

    with open("Fast_Changelog.md", "w") as f: 
      f.write(file_content)
  