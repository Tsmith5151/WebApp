from django import forms

from .models import SignUp

class ContactForm(forms.Form):
	name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		if not extension in ["com", "edu", "net","org"]: 
			raise forms.ValidationError("Please use valid E-mail Address")
		return email

class SignUpForm(forms.ModelForm):
	class Meta:
			model = SignUp
			fields =['name','email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		if not extension in ["com", "edu", "net","org"]: 
			raise forms.ValidationError("Please use valid E-mail Address")
		return email

