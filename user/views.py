from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile
import smtplib
from django.contrib.auth import authenticate

# Create your views here.
from .forms import UserForm,ProfileForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login
from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name='user/home.html'

def sent_email(rec,name):
	mail=smtplib.SMTP('smtp.gmail.com',587)
	mail.ehlo()
	mail.starttls()
	mail.login('','')
	mail.sendmail('canvashcode@gmail.com',str(rec),f"Congratulations {name}! You have been registered with Greenify.")
	mail.close()


def register(request):
	if request.method=='POST':
		name=request.POST.get('name')
		email=request.POST.get('email')
		phone=request.POST.get('phone')
		city=request.POST.get('city')
		password=request.POST.get('password')
		user=User.objects.create_user(username=email,email=email,password=password)
		profile=Profile(user=user,phone=phone,city=city)
		profile.save()
		user=authenticate(username=email,password=password)
		login(request,user)
		sent_email(email,name)
		print("yes")
		return redirect('home')

	return render(request,'user/register.html')

def user_login(request):
	if request.method=='POST':
		email=request.POST.get('email')
		password=request.POST.get('password')
		print(email,password)
		user = authenticate(username=email, password=password)
		if user:
			if user.is_active:
				login(request, user)
				
				return redirect('home')
				
	return render(request,'user/login.html')