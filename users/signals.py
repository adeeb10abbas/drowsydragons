from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

from random import randint


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        rand_pi_id = random_with_N_digits(6)
        Profile.objects.create(user=instance, piId= rand_pi_id)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()



def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)