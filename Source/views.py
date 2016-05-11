from django.shortcuts import render


# Create your views here.

def Races(request):
		
	return render(request,"Races.html", {})

def About(request):
		
	return render(request,"About.html", {})