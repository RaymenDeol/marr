from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class link(models.Model):
	url = models.CharField(unique=True, max_length=200)
	title = models.CharField(max_length=50)
	content = models.TextField()

class user_picture(models.Model):
	title = models.CharField(max_length=50, unique=True)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='user_images')


