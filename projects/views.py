from django.shortcuts import render

def home(request, year, month):
	name = "Barnes"
	return render(request,
		'home.html', {
		"name": name,
		"year": year,
		"month": month,
		})
