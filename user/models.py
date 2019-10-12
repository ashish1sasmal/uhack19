from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	
	phone=models.CharField(max_length=10)
	city=models.CharField(max_length=50)
	country=models.CharField(max_length=60)
	def __str__(self):
		return f'{self.user.username} Profile'