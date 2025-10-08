import requests
import datetime as dt

api_key = '4069f9c375a9314ad2aa3ea923933283'

My_Lat = 51.050407
MY_Lon = 13.737262
Days = 10
Unit = 'metric'

parameters = {
    'lat': My_Lat,
    'lon': MY_Lon,
    'appid': api_key,
    'cnt': Days,
    'units': Unit

}

response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for day in data['list']:
    weather_id = day['weather'][0]['id']
    if int(weather_id) < 700:
        will_rain = True
        
if will_rain:
    print("Bring an umbrella")

