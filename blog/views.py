from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .models import Drowsy
from users.models import Profile


def landing(request):
    return render(request, 'blog/index.html')


def driver_is_sleepy(request): #adeeb sends us shit here 
    input_data = {
        "piId": 806103,
    }

    # try: 
    drowsy_user = Profile.objects.get(piId=input_data['piId']) #change this
    drowsy_obj = Drowsy.objects.create(driver=drowsy_user) #drowsy log
        #play_music(user_details)
    # except:
    #     print("This pi is not registered with us.")
 
    return HttpResponse("Music has been played for a user whow as drowsy while driving")

def dashboard(request):
    context = {
        "name": "anna", #read from database
    }
    return render(request, 'blog/dashboard.html', context)

def register_spotify():
    pass

def control_spotify():
    pass

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


