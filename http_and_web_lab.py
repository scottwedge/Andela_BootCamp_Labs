import requests
import json

api_key = '92f135e73e13bdd8f59b57347820f8af'

def get_weather(city):
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+api_key)
	weather_info = r.json()
	return weather_info

while True:
	desired_city = input('Please enter a city name and I will give you the current weather.\nPress enter without any text to exit: ').lower()
	if desired_city == '':
		break
	else:
		city_weather = get_weather(desired_city)
		if city_weather['name'].lower() == desired_city.lower():
			print ('\nThe weather in ' + city_weather['name'] + ' is currently: ' + city_weather['weather'][0]['description'])
			print ('Here is some more information on '+ city_weather['name'] + ' (Powered by openweathermaps.org')
			print ('Temperature (in Celsius): ' + str(city_weather['main']['temp'] - 273))
			print ('Humidity: ' + str(city_weather['main']['humidity']))
			print ('Pressure: ' + str(city_weather['main']['pressure']))
			print ()
		else:
			print("Sorry. I couldn't get information for that city.\n")