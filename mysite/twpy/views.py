from django.shortcuts import render
from django.http import HttpResponse

from .forms import TwForm

import tweepy 

consumer_key = '6vWSFssZSZ6ca87IUeSkV1VR2'
consumer_secret = 'zftYif2YKWnkeJblQGqIMst5q50gZ1qusYubZ73Rstp6fkO0bT'
access_token = '3755330536-ME2ulUmQGAO7ZG2I9znrvQjQDsOlTEavpauCynN'
access_token_secret = 'LfptIr4rQa9qKB1Lt3j2FxtThKwIaePQopz1JqwXaQCyW'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TwForm(request.POST)
        
        if form.is_valid():
            user = api.get_user(screen_name=request.POST['screen_name'])
            value = str(user.friends_count)
            return HttpResponse(value)
    else:
        form = TwForm()
        return render(request, 'name.html', {'form':form})
