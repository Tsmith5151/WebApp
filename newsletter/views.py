from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm, SignUpForm

# Create your views here.

def home(request):
	title = 'Welcome'
	#if request.user.is_authenticated():
	#	title = "Welcome %s" %(request.user)
	# Add Form
	form = SignUpForm(request.POST or None)
	context = {
			"form": form
		}

	if form.is_valid():
		instance = form.save(commit=False)
		name = form.cleaned_data.get("name")
		if not name:
			name = "New Full Name"
		instance.name = name
		instance.save()
		context = {
				"title": "Thank You"

			}
	return render(request,"home.html", context)

def contact(request):
	title = 'Contact Us'
	form = ContactForm(request.POST or None)
	if form.is_valid():
		#Alt. way...example when have multiple forms
		#for key, value in form.cleaned_data.iteritems():
		#	print key, value
		form_email = form.cleaned_data.get("email")
		form_name = form.cleaned_data.get("name")
		form_message = form.cleaned_data.get("message")
		#print email, name, message
		# fail silently = true is saving in the database
		subject = 'Site Contact From'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email,'Trace@inpersona3d.com']
		contact_message = "%s: %s via %s"%(
			form_name, 
			form_message, 
			form_email)
		#html_message = """
		#<h1>Thank You</h1>
		#"""
		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				#html_message = html_message
				fail_silently=True)
	context = {
		"form": form,
	}

	return render(request, "forms.html", context)






