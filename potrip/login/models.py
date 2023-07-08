from django.db import models
from django.utils import timezone

#username+password
class User(models.Model):
    username = models.CharField(max_length=255)  
    password = models.CharField(max_length=255)  
    create_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.username