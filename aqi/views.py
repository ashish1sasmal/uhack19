from django.shortcuts import render
import string
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
	return((json_data['data'])['aqi'])

def aqicheck(request):
	a=request.user.profile.city
	a=a.replace(' ','')
	print(a)
	return render(request,'aqi/check.html',{'info':int(airindex(str(a)))})

