from django.shortcuts import render
from django.http import HttpResponse
from .models import link
from .models import user_picture
from django.template import loader, Context
from django.contrib.auth.decorators import login_required
from django.template import RequestContext




@login_required
def user_home(request):
	return render(request, 'user_home.html')



@login_required
def website_links(request):
	websites = {}
	i = link.objects.count()+1 #Added 1 to match Django Auto Increment ID which starts at 1



	for x in range(1,i):
		website_id = link.objects.get(id=x)
		name = "website" + str(x) 
		websites[name] = website_id.url
	return render(request, 'user_links.html', {'websites':websites})

@login_required
def user_pictures(request):
    pictures = user_picture.objects.all()
    return render(request, 'user_pictures.html', {'pictures': pictures})

