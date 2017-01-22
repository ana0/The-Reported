from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, UpdateView
from django.views.generic import FormView
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.forms import ValidationError
from.forms import SelectMovieForm

from django.contrib.auth.models import User
from .models import Viewed, Report, Movie

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .secrets import YoutubeApiKey

import datetime
import requests
import json

def index(request):
    context = {}
    return render(request, 'movietracker/index.html', context)

class CreateNewUser(CreateView):
    """User sign up page"""
    model = User
    form_class = UserCreationForm
    success_url = 'profile'
    template_name ='registration/register.html'

class ViewHistoryList(ListView):
    """Account home pages, displays view history"""
    template_name = 'movietracker/profile.html'

    def get_queryset(self):
        return Viewed.objects.filter(user=self.request.user)
    
class CreateReport(CreateView):
    """Write a report"""
    model = Report
    fields = ['movie', 'review', 'rating']
    template_name = 'movietracker/create_report.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateReport, self).form_valid(form)

class AddMovie(CreateView):
    """Add a movie to the database from youtube by url"""
    model = Movie
    fields = ['url']
    template_name = 'movietracker/add_movie.html'
    success_url = reverse_lazy('watchmovie')

    def form_valid(self, form):
        #needs error checking on urls that dont's have the '='
        #should override the clean method here actually
        #first we extract the video id from the url by string mechanics
        video_id = form.instance.url.split("=")[1]
        video_url = ("https://www.googleapis.com/youtube/v3/videos?part="
            "snippet&id=" + video_id + "&key=" + YoutubeApiKey)
        try:
            #try to request the video info from youtube, raise an error if 400 
            #or 500 codes
            ask_youtube = requests.get(video_url)
            ask_youtube.raise_for_status()
            parse_json = json.loads(ask_youtube.text)
            if len(parse_json["items"]) > 0:
                #if items is > 0 the video id corresponded to an actual video
                #so we add it to the db
                title = parse_json["items"][0]["snippet"]["title"]
                form.instance.title = title
                self.request.session["video_id"] = video_id
                form.instance.video_id = video_id
            else:
                #redirect if not a valid video
                return render(self.request, 'movietracker/error.html')
        except requests.exceptions.HTTPError as err:
            #if youtube's api is down, or the internet itself, also redirect
            return render(self.request, 'movietracker/error.html')
        return super(AddMovie, self).form_valid(form)

class SelectMovie(FormView):
    """Select a movie to watch from the existing list of movies"""
    form_class = SelectMovieForm
    template_name = 'movietracker/select_movie.html'
    success_url = reverse_lazy('watchmovie')

    def form_valid(self, form):
        chosen_movie = Movie.objects.get(title=form.cleaned_data['movies'])
        self.request.session["video_id"] = chosen_movie.video_id
        return super(SelectMovie, self).form_valid(form)

class WatchMovie(CreateView):
    """Watch an embedded youtube movie"""
    model = Viewed
    fields = []
    template_name = 'movietracker/watch_movie.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super(WatchMovie, self).get_context_data(**kwargs)
        video_id = self.request.session["video_id"]
        context['youtube_url'] = "https://www.youtube.com/embed/" + video_id
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        video_id = self.request.session["video_id"]
        movie = Movie.objects.get(video_id=video_id)
        form.instance.movie = movie
        return super(WatchMovie, self).form_valid(form)
