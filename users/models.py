from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    piId = models.IntegerField(default=0)
    spotify_pref = models.TextField()


    def __str__(self):
        return f'{self.user.username} Profile'
