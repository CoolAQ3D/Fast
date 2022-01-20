
#for testing purposes
def test():
  fast_data = txt_to_list("fast_data.txt")
  print(fast_data)

def txt_to_list(file_path):

    remove_hashtag = []
    data_only = []

    try:
        user_data =open(file_path,"r")
        lines = user_data.read().split('\n')

        #remove lines that starts with #
        for line in lines:
          if not(line.startswith("#")): 
            remove_hashtag.append(line)
        
        #next remove empty lines ""
        for line in remove_hashtag:
          if len(line) != 0:
            data_only.append(line)
            

        return data_only

    except Exception as e:
        print(e)