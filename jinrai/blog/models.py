from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save	
from django.dispatch import receiver




class BlogPost(models.Model): 
	title					= models.CharField(max_length=50, null=False, blank=False)
	body					= models.CharField(max_length=5000, null=False, blank=False)
	#image_url 				= models.URLField(max_length=500, blank=True, null=True)  # Field to store image URL
	date_published			= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated			= models.DateTimeField(auto_now=True, verbose_name="date updated")
	author					= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	slug					= models.SlugField(blank=True, unique=True)

def __str__(self):
	return self.title

@receiver(post_delete, sender=BlogPost)
# def submission_delete(sender, instance)  this deleted the image stored if there is one uploaded.
# 	instance.image.delete(False)

def pre_save_bloc_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.author.username + "-" + instance.title)

pre_save.connect(pre_save_bloc_post_receiver, sender=BlogPost)