from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def index(request):
    url = 'https://twitter.com/toptweets?lang=en'
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")
    tweeter_list = {}
    for name, tweet in zip(s.findAll(attrs={'class': 'fullname show-popup-with'
                                                     '-id u-textTruncate'}),
                           s.findAll(attrs={'class': 'TweetTextSize'})):
        tweeter_list[name.text] = tweet.text
    context = {
        'tweets': tweeter_list
    }
    return render(request, 'index.html', context)
