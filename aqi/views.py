from django.shortcuts import render

import urllib.parse
import requests
from  geopy.geocoders import Nominatim

from django.views.generic import TemplateView,ListView
from django.contrib.auth.models import User
# Create your views here.

# def geoloc(city):
# 	main_api='https://api.waqi.info/feed/geo::lat;:lng/?token=2b64c5a328bd82843e990c3f94ee25167cc3f0d6'
# 	main_api='https://api.waqi.info/search/?keyword='+city+'&token=2b64c5a328bd82843e990c3f94ee25167cc3f0d6'
# 	json_data=requests.get(main_api).json()
# 	return((json_data['data'])['aqi'])

def airindex(city):
	
	geolocator = Nominatim()
	country ="india"
	loc = geolocator.geocode(city+','+ country)
	main_api='https://api.waqi.info/feed/geo::lat;:lng/?token=2b64c5a328bd82843e990c3f94ee25167cc3f0d6'
	main_api='https://api.waqi.info/feed/geo:'+str(loc.latitude)+';'+str(loc.longitude)+'/?token=2b64c5a328bd82843e990c3f94ee25167cc3f0d6'

	# main_api='https://api.waqi.info/search/?keyword='+city+'&token=2b64c5a328bd82843e990c3f94ee25167cc3f0d6'


	json_data=requests.get(main_api).json()
	return(json_data)

def aqicheck(request):
	a=request.user.profile.city
	b=a.replace(' ','')
	json_data=airindex(b)
	aqi=json_data['data']['aqi']
	print(aqi)
	t=json_data['data']['time']['s']
	co=json_data['data']['iaqi']['co']['v']
	print(co)
	#no2=json_data['data']['iaqi']['no2']['v']
	o3=json_data['data']['iaqi']['o3']['v']
	pm10=json_data['data']['iaqi']['pm10']['v']
	so2=json_data['data']['iaqi']['so2']['v']
	return render(request,'aqi/check.html',{'time':t,'city':a,'aqi':aqi,'co':co,'no':8,'o':o3,'pm':pm10,'so':so2})

