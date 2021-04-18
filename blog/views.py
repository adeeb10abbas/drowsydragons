from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages

from .models import Drowsy


def landing(request):
    return render(request, 'blog/grand-pro-opl/index.html')


def driver_is_sleepy(request): #adeeb sends us shit here 
    input_data = {
        "piId": 1,
        "speed": 2,
        "location": 3, 
    }

    drowsy_user = User.objects.get(piId=input_data['piId'])
    # drowsyUser = Drowsy.objects.create(

    #         )
    #call spotify API- turn the music on 
    return HttpResponse("yo")

#when user is logged in
def dashboard(request):
    return render(request, 'blog/dashboard.html')

def register_spotify(request):
    import spotipy
    from spotipy import oauth2
    import requests

    CLIENT_ID = "fec22cf923c04b9eae0a62c19bfcd731"
    CLIENT_SECRET = "bf61a4918571412f920ea14190d8d227"

    credentials = oauth2.SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET, redirect_uri="http://127.0.0.1:8000/dashboard/confirmspotify", scope="user-read-playback-state, user-modify-playback-state")

    token = credentials.get_access_token()

    spotify = spotipy.Spotify(auth=token)

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+token.get('access_token'),
    }
    print(headers)
    return render(request, 'blog/dashboard.html')

def confirm_spotify(request):
    import requests
    import base64

    CLIENT_ID = "fec22cf923c04b9eae0a62c19bfcd731"
    CLIENT_SECRET = "bf61a4918571412f920ea14190d8d227"

    code = str(request.GET['code'])
    messages.info(request, 'code: '+code)

    #auth_str = 'Basic '+CLIENT_ID+":"+CLIENT_SECRET
    
    #headers = {
    #    'Authorization': auth_str,
    #}

    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://127.0.0.1:8000/dashboard/confirmspotify'
    }

    response = requests.post('https://accounts.spotify.com/api/token', auth=(CLIENT_ID, CLIENT_SECRET), data=data)
    messages.info(request, 'You have successfully registered with Spotify.')
    access_token = response.json()['access_token']

    return render(request, 'blog/dashboard.html')

def control_spotify():
    pass


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})