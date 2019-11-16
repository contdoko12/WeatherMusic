import pyowm
P=input('input a city')
owm = pyowm.OWM('7f79fb28dc1e878a119f011470868208')
if P == 'New York' or 'Tampa':
    location = owm.weather_at_place(P)
    weather = location.get_weather()


print(weather)

temp = weather.get_temperature('fahrenheit')
 

print(temp)


