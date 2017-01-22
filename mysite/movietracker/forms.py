from django import forms

from .models import Movie

class SelectMovieForm(forms.Form):
    movies = forms.ModelChoiceField(queryset=Movie.objects.all().order_by('title'))