import urllib.request
import json



def get_weather(lat,lon):
  #"Get the weather using lat and long from get_iss"
  key='943b18b8619bf62947d941faaa0a8e37'
  url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result
  