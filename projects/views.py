from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
	name = "Barnes"
	month = month.capitalize()

# Convert month from name
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)

# Create a calendar
	cal = HTMLCalendar().formatmonth(year, month_number)
	now = datetime.now()

	time = now.strftime('%I:%M %p')

	return render(request,
		'home.html', {
		"name": name,
		"year": year,
		"month": month,
		"month_number": month_number,
		"cal" : cal, 
		"time" : time,
		})