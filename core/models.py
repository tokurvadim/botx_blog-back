from django.db import models

class Users(models.Model):
    id = models.BigIntegerField(primary_key=True)