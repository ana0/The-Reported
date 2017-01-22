from django.contrib import admin

# Register your models here.

from .models import Movie, Viewed, Report

admin.site.register(Movie)
admin.site.register(Viewed)
admin.site.register(Report)