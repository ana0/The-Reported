from django.db import models

from django.contrib.auth.models import User


class Movie(models.Model):
    #Should probably refactor and use video id as the primary key
    url = models.URLField('Movie location')
    title = models.CharField('Title', max_length=300)
    video_id = models.CharField('Video id', max_length=10)
    # let's leave this as a stretch goal for now . . .
    # length = models.DurationField('Length of movie')
    
    def __str__(self):
        return self.title

class Viewed(models.Model):
    watched_date = models.DateField('Watched date', auto_now_add=True)
    started_watching = models.TimeField('Began watching', auto_now_add=True)
    # finished_watching = models.TimeField('Stopped watching', auto_now=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.watched_date) + " " + self.movie.title 

class Report(models.Model):
    review = models.TextField('Review', max_length=3000)
    rating = models.IntegerField('Rating', choices=[(i, i) for i in range(1, 6)])
    created_date = models.DateField('Published date', auto_now_add=True)
    update_date = models.DateField('Updated date', auto_now=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title + ": \"" + self.review[0:30] + "\""
