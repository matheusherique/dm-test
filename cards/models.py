from django.db import models
from django.conf import settings
from api.models import User

class Solicitation(models.Model):
    credit = models.IntegerField(default=0)
    fk_users = models.ForeignKey(User, 
        on_delete=models.CASCADE, 
        related_name= 'fk_users_id')