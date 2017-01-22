from django.conf.urls import url

from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/profile/$', login_required(views.ViewHistoryList.as_view()), 
        name='profile'),
    url(r'^register/', views.CreateNewUser.as_view(), name='register'),
    url(r'^create_report/', login_required(views.CreateReport.as_view()), 
        name='createreport'),
    url(r'^add_movie/', login_required(views.AddMovie.as_view()), 
        name='addmovie'),
    url(r'^select_movie/', login_required(views.SelectMovie.as_view()), 
        name='selectmovie'),
    url(r'^watch_movie/', login_required(views.WatchMovie.as_view()), 
        name='watchmovie'),
]