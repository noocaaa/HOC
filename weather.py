import pyowm # Python Open Weather
from geopy.geocoders import Nominatim

key = '61be56cc6f5a837ea95f719805978b70'
city = 'London'

#obtener latitud y longitud

geolocator = Nominatim(user_agent='myapplication')
location = geolocator.geocode(city)

LON = location.longitude
LAT = location.latitude

#obtener informacion tiempo

openMap = pyowm.OWM(key)   
openMaps = openMap.weather_manager()                
tiempo = openMaps.weather_at_place(city)  
data = tiempo.weather                  

print ('-----------------------------------------------------------')

print ('STATUS: ', data.detailed_status)
print('WIND: ', data.wind)   
print('HUMIDITY: ', data.humidity)     
print('TEMPERATURE IN CELSIUS: ', data.temperature('celsius')) 
print('RAIN: ', data.rain)    
print('HEAT INDEX: ', data.heat_index) 
print('CLOUDS: ', data.clouds)

print ('-----------------------------------------------------------')

#FORECAST WEATHER

one_call = openMaps.one_call(lat=LAT, lon=LON)

print ('During the day we are going to have', one_call.forecast_daily[0].detailed_status) #prediccion para el dia

print ('-----------------------------------------------------------')

#WHAT WE TINK THAT WE WOULD NEED TO READ OUT LOUD

#temperatura en C
print ('----- TEMPERATURE -----')

temp = data.temperature('celsius')      
print ("Average Temp. Currently ", temp['temp'])
print ("Max Temp. Currently ", temp['temp_max'])
print ("Min Temp. Currently ", temp['temp_min']) 
print ("Feels like Temp", temp['feels_like'])

print ('----- RAIN -----')

if data.rain == {}:
	print ("It is not raining right now.")
else:
	print("It is raining right now.")
	
print ('----- HUMIDITY -----')

print('The actual humidity is ', data.humidity)     


