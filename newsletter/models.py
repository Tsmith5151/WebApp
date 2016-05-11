from __future__ import unicode_literals

from django.db import models

from datetime import date, datetime

# Create your models here.
class SignUp(models.Model):
	#email
	email = models.EmailField()
	#full name (character field: numbers or letters)
	name = models.CharField(max_length=20, blank=False, null=True)
	#when did it occur 
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):#_str_
		return str(self.email)
