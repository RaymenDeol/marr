from django.urls import path
from . import views
from django.contrib.auth.views import login

app_name = 'resource_library'

urlpatterns = [
	path('login/', login, name='login'),
	path('user_home/', views.user_home, name='user_home'),
	path('user_links/', views.website_links, name='user_links'),
]
