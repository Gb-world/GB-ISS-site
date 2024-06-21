#find the location of iss
#weather information
#reverse geolocation (we lat and lon and the address or country name)
#distance between you and ISS
#rest countries api
#The Flag of the country
from flask import Flask, render_template
from get_iss import iss_loc
from get_weather import get_weather
from get_address import address
from get_distance import dist
from get_country import country

app = Flask('app')


@app.route('/')
def index():
  #Extract latitude and longitude from the API
  data = iss_loc()
  lat, lon, isslocation = data[0], data[1], data[2]
  flag = ""

  #Weather
  #Getting weather information using the extracted latitude and longitude
  weather = get_weather(lat, lon)
  #print(weather)
  temp_c = round(weather["main"]["temp"] - 273.15, 2)
  description = weather["weather"][0]["description"]
  #print(str(temp_c)+" C " + description)
  wea_desc = str(temp_c) + " Celcius " +"," +description

  # address reverse geolocation
  add = address(lat, lon)
  # print(add)
  # Print the Country Code
  #print("Country Code is : ",add["countryCode"])

  #distance from ISS
  distance = dist(lat, lon, 46.5290876, -80.9432954)
  #print(f"You are {distance} km from the ISS")
  dist_message = f"You are {distance} km from the ISS"

  #Extracting of the flag and country name of the ISS location
  if (add["countryCode"] == ""):
    #print("ISS is over water")
    countryname = 'ISS IS OVER WATER BODY'
    #flag = 'ISS IS OVER WATER BODY'
  
  else:
    location = add["countryCode"]
    countryname = "The ISS is currently in "  + add["countryName"]
    print("Country Code is : ", add["countryCode"])
    flag = country(location)[0]["flags"]["png"]
    #print(flag)
  data = [lat, lon, isslocation, wea_desc, dist_message, countryname]
  return render_template("index.html",flag=flag, data = data
                        )


app.run(host='0.0.0.0', port=8080)
