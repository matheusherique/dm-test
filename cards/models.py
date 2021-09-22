from django.db import models
from django.conf import settings

class Solicitation(models.Model):
    credit = models.IntegerField(default=0)
    fk_users = models.ForeignKey(settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name= 'fk_users_id')