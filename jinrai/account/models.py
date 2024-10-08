from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class MyAccountManager(BaseUserManager): ##Custom Account Manager
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError("When registering you MUST have an email.")
		if not username:
			raise ValueError("When registering you MUST provide a username.")

		user =	self.model(
				email=self.normalize_email(email),
				username=username,
			)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user =	self.create_user(
				email=self.normalize_email(email),
				password=password,
				username=username,
			)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser, PermissionsMixin):
	email						= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username					= models.CharField(max_length=60, unique=True)
	date_joined					= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login					= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin					= models.BooleanField(default=False)
	is_active					= models.BooleanField(default=True)
	is_staff					= models.BooleanField(default=False)
	is_superuser				= models.BooleanField(default=False)

	USERNAME_FIELD = 'email'   #YOU HAVE TO SET USERNAME_FIELD to whatever you want the user to log in with. 
	REQUIRED_FIELDS = ['username'] #iF YOU WANT THEM TO INCLUDE A NAME for required fields for when registering
	# example ['username', 'email']
# Create your models here.

	objects = MyAccountManager()



def __str__(self):
	return self.email ##you can change to username if you want

def has_perm(self, perm, obj=None):
	return self.its_admin

def has_module_perms(self, app_label):
	return True