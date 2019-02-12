"""top_trending_apps URL Configuration
"""
from django.contrib import admin
from django.urls import include, path
import twitter_app.urls
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('twitter_app/', include(twitter_app.urls, namespace='twitter_app')),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls)
]
