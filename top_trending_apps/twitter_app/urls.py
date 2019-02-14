from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'twitter_app/'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
]
