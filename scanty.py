import pyowm

owm = pyowm.OWM('e2a18ac7e9c92a921296aa7e8a1bc55f')
observation = owm.weather_at_place('Koforidua')
w = observation.get_weather()

print(w.get_wind())
print(w.get_humidity())

