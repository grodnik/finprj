from django.contrib import admin
from .models import Project
from .models import Expense

admin.site.register(Project)
admin.site.register(Expense)