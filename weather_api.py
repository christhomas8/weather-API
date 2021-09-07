#python3.8 

import json, requests, sys, time, math

APPID = '<--------------------->'
print("API key stored")
print()

"""
#compute location from command line arguments
if len(sys.argv) < 2:
	print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
	sys.exit()
"""

#location = ' '.join(sys.argv[1:])
city = input("What City? ")
print('City stored!')
print()
country = input("What Country? ")
print('Country stored!')
print()

# Download the JSON data from OpenWeatherMap.org's API.
url = 'https://api.openweathermap.org/data/2.5/weather?q=%s,%s&appid=%s'%(city,country,APPID)
#url = 'https://api.openweathermap.org/data/2.5/weather?q=dallas,tx,usa&appid=<------------------------>'
print('The url is: \n',url)
print()

time.sleep(2)

print('checking status... ')
response = requests.get(url)
print()

response.raise_for_status()
print('status determined')
print()

print("JSON Data:")
print(response.text)
print()

weatherData = json.loads(response.text)
w = weatherData['weather']
m = weatherData['main']
print(w)
print()
print(m)
print()


print(w[0]['main'])

avg_t = m['temp']
feel_temp = m['feels_like']

def kelvin(x):
	temperature = 9*float(x)/5 - 459.67
	ans = round(temperature,1)
	return ans

#temp = 9*float(m['temp'])/5-(460)
#print(temp)

print("The temperature in "+city+" is: "+str(kelvin(avg_t))+" deg F")
print("The temperature in "+city+" feels like: "+str(kelvin(feel_temp))+" deg F")

#print(m['feels_like'])

"""
weatherData = json.loads(response.text)
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
"""
