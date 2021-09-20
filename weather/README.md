# Weather

To use this weather script you must set two environment varibles. 

SWIFTBAR_WEATHER_LOCATIONS must be one or more OpenWeatherMap locations. These codes are in the URL when viewing the weather for a given city.

For example, the city of London GB has the location code 2643743 and can be viewed at the URL https://openweathermap.org/city/2643743. 

SWIFTBAR_WEATHER_API_KEY is your personal API key and can be seen [on your OpenWeatherMap Account page](https://home.openweathermap.org/api_keys).

Here's an example configuration where the locations of interest are:

* [London, England, United Kingdon](https://openweathermap.org/city/2643743)
* [London, Ontario, Canada](https://openweathermap.org/city/6058560)
* [London, Ohio, United States](https://openweathermap.org/city/4517009)
* [London, California, United States](https://openweathermap.org/city/5367815)

```
SWIFTBAR_WEATHER_LOCATIONS=2643743 6058560 4517009 5367815
SWIFTBAR_WEATHER_API_KEY=1234567890
```