from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from users.models import Profile
 

import uuid 
#each class is a table. 
class Drowsy(models.Model):
    drowsyreq = models.AutoField(primary_key=True, default=uuid.uuid1)
    date_posted = models.DateTimeField(default=timezone.now)
    driver = models.ForeignKey(Profile, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title

