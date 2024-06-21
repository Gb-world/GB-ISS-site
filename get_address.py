import urllib.request
import json


def address(lat,lon):
  # Use of the geocoding API to get the address of the ISS
  url=f'https://api.bigdatacloud.net/data/reverse-geocode-client?latitude={lat}&longitude={lon}&localityLanguage=en'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result