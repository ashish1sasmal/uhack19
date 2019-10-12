
from django.urls import path
from . import views

urlpatterns = [
    path('check/',views.aqicheck,name='check'),
]
