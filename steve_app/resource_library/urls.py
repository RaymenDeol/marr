from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'resource_library'

urlpatterns = [
	path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
	path('user_home/', views.user_home, name='user_home'),
	path('user_links/', views.website_links, name='user_links'),
    path('user_pictures/', views.user_pictures, name='user_pictures'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
