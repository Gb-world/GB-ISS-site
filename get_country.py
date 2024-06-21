import urllib.request
import json


def country(name):
  #Use of API to get details about the country 
  url = f'https://restcountries.com/v3.1/alpha/{name}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result