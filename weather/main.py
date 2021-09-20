#!/usr/bin/env python
# -*- coding: utf-8 -*-

# <bitbar.title>Weather - OpenWeatherMap</bitbar.title>
# <bitbar.version>v1.2</bitbar.version>
# <bitbar.author>rmwphd</bitbar.author>
# <bitbar.author.github>rmwphd</bitbar.author.github>
# <bitbar.desc>Grabs simple weather information from openweathermap. Needs configuration for location and API key.</bitbar.desc>
# <bitbar.dependencies>python,SF Symbols</bitbar.dependencies>

import json
import urllib3
import traceback
import time
import os

def get_wx(location, api_key, units):

  if api_key == "":
    return False
  try:
    wurl = "https://api.openweathermap.org/data/2.5/weather?id=" + location + "&appid=" + api_key + "&units=" + units
    http = urllib3.PoolManager()
    response = http.request('GET', wurl)
    rawJson = response.data.decode('utf-8')
    fjson = json.loads(rawJson)
  except Exception as e:
    return False


  try:
    weather_data = {
      'temperature': str(int(round(fjson['main']['temp']))),
      'condition': str(fjson['weather'][0]['description']),
      'id': fjson['weather'][0]['id'],
      'city': fjson['name'],
      'feelslike': str(int(round(fjson['main']['feels_like']))),
      'unit': '°',
      'high': str(int(round(fjson['main']['temp_max'])))
    }
    if time.time() < fjson['sys']['sunrise']:
      weather_data['night'] = True
    elif time.time() > fjson['sys']['sunset']:
      weather_data['night'] =  True
    else:
      weather_data['night'] = False
  except KeyError:
    return False

  return weather_data

def render_wx(location, api_key, units, main):
  weather_data = get_wx(location, api_key, units)
  emoji_dict = {
  200 : ":cloud.sun.bolt.fill:",  201 : ":cloud.bolt.rain.fill:",  202 : ":cloud.bolt.rain.fill:",  210 : ":cloud.bolt.rain.fill:",  211 : ":cloud.bolt.rain.fill:",  212 : ":cloud.bolt.rain.fill:",  221 : ":cloud.bolt.rain.fill:",  230 : ":cloud.bolt.rain.fill:",  231 : ":cloud.bolt.rain.fill:",  232 : ":cloud.bolt.rain.fill:",
  300 : "cloud.sun.rain.fill",  301 : ":cloud.drizzle.fill:",  302 : ":cloud.drizzle.fill:",  310 : ":cloud.drizzle.fill:",  311 : ":cloud.drizzle.fill:",  312 : ":cloud.drizzle.fill:",  313 : ":cloud.drizzle.fill:",  314 : ":cloud.drizzle.fill:",  321 : ":cloud.drizzle.fill:",
  500 : ":cloud.sun.rain.fill:",  501 : ":cloud.rain.fill:",  502 : ":cloud.heavyrain.fill:",  503 : ":cloud.heavyrain.fill:",  504 : ":cloud.heavyrain.fill:",  511 : ":cloud.hail.fill:",  520 : ":cloud.heavyrain.fill:",  521 : ":cloud.heavyrain.fill:",  522 : ":cloud.heavyrain.fill:",  531 : ":cloud.heavyrain.fill:",
  600 : ":snow:",  601 : ":snow:",  602 : ":wind.snow:",  611 : ":snow:",  612 : ":snow:",  613 : ":snow:",  615 : ":snow:",  616 : ":snow:",  620 : ":snow:",  621 : ":snow:",  622 : ":snow:",
  701 : ":cloud.fog.fill:",  711 : ":cloud.fog.fill:",  721 : ":cloud.fog.fill:",  731 : ":cloud.fog.fill:",  741 : ":cloud.fog.fill:",  751 : ":cloud.fog.fill:",  761 : ":cloud.fog.fill:",  762 : ":cloud.fog.fill:",  771 : ":wind:",
  781 : ":tornado:",
  800 : ":sun.max.fill:",
  801 : ":cloud.sun.fill:",  802 : ":cloud.sun.fill:",  803 : ":cloud.fill:",  804 : ":smoke.fill:",
  }
  if weather_data['night']:
    emoji_dict[200] = ":cloud.moon.bolt.fill:"
    emoji_dict[300] = ":cloud.moon.rain.fill:"
    emoji_dict[500] = ":cloud.moon.rain.fill:"
    emoji_dict[800] = ":moon.fill:"
    emoji_dict[801] = ":cloud.moon.fill:"
    emoji_dict[802] = ":cloud.moon.fill:"

  tridash = '\n' + '---' + '\n'

  if weather_data is False:
    return 'No weather data' + tridash + 'Could not get weather; Maybe check API key or location?'

  emojiweather = emoji_dict[weather_data['id']]

  #weather_data['condition'] + ' ' +
  emoji_t = '' + emojiweather + ' ' + weather_data['temperature'] + weather_data['unit']
  condi = [x.capitalize() for x in  weather_data['condition'].split(' ')]
  weatherInfo = emoji_t + tridash + ' '.join(condi) + "| symbolize=true\n" + "Feels like " + weather_data['feelslike'] + "° in " + weather_data['city'] + "\nTodays high: " + weather_data['high'] + "°\nView online | href=https://openweathermap.org/city/" + location
  if main is False:
    weatherInfo = emoji_t + "\n" + ' '.join(condi) + "| symbolize=true\n" + "Feels like " + weather_data['feelslike'] + "° in " + weather_data['city'] + "\nTodays high: " + weather_data['high'] + "°\nView online | href=https://openweathermap.org/city/" + location
  return weatherInfo

locations = str(os.environ['SWIFTBAR_WEATHER_LOCATIONS']).split(" ")
api_key = os.environ['SWIFTBAR_WEATHER_API_KEY']
units = 'metric' # kelvin, metric, imperial
i = 0
for location in locations:
  if i > 0:
    main = False
    print(render_wx(location, api_key, units, main))
  else:
    main = True
    print(render_wx(location, api_key, units, main))
  i = i + 1