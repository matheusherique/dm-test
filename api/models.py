from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import random

class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=100)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return "{}".format(self.email)
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, related_name='profile')
    income = models.IntegerField(default=0)
    score = models.IntegerField(default=random.randint(1, 999), 
        editable=False)