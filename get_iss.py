import urllib.request
import json


def iss_loc():
  # Use API to get the location of the ISS
  url = "http://api.open-notify.org/iss-now.json"
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  
  #print(result)
  # Pass the Latitude and Longitiude to the google maps
  
  
  lat = result['iss_position']['latitude']
  lon = result['iss_position']['longitude']
  isslocation = "https://www.google.com/maps/place/" + lat + "+" + lon 
 
  #print("google map", "https://www.google.com/maps/place/" + lat + "+" + lon )
  return lat,lon,isslocation