from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="accountPP", null=True, blank=True) # or whatever

    def __str__(self):
        return self.user.email