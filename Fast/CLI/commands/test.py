
#for testing purposes
def test():
  print('hi')

  import urllib.request
  import json


  ips = ['104.197.76.221']


  for ip in ips:
          with urllib.request.urlopen("https://geolocation-db.com/jsonp/"+ip) as url:
                  data = url.read().decode()
                  data = data.split("(")[1].strip(")")
                  print(data)