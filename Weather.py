import pyowm

owm = pyowm.OWM('7f79fb28dc1e878a119f011470868208')

location = owm.weather_at_place('New York')
weather = location.get_weather()

print(weather)

temp = weather.get_temperature('fahrenheit')

print(temp)



