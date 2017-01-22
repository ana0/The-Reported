from django.shortcuts import render
from django.views.generic import View, ListView
from django.db.models import Count, Avg

from movietracker.models import Viewed, Report, Movie


class MakeReport(ListView):
    """Prints a report of all views, and average ratings"""
    template_name = 'movietracker/admin_report.html'

    def get_queryset(self):
        return Movie.objects.annotate(num_views=Count('viewed'), 
        avg_rating=Avg('report__rating'))
        