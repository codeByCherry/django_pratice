from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    birth = models.DateField(null=True)
    phone = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "user_profile:" + self.user.username
