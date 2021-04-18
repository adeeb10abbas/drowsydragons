from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

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

def register_spotify():
    pass

def control_spotify():
    pass


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
