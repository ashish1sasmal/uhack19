from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name='user/home.html'

def register(request):
	if request.method=='POST':
		form = UserForm(data=request.POST)
		profile_form=ProfileForm(data=request.POST)
		if form.is_valid() and profile_form.is_valid():
			
				user=form.save(commit=False)
				user.username=form.cleaned_data.get('email')
				user.save()
				profile=profile_form.save(commit=False)
				profile.user=user
				profile.save()
				# name = form.cleaned_data.get('username')
				# user=form.save(commit=False)
				# user.username=name
				
				
				return redirect('login')
	else:
		form = UserForm()
		profile_form=ProfileForm()

	return render(request,'user/register.html',{'form':form,'profile_form':profile_form})