from django.db import models

class LoginUser(models.Model):
    user = models.CharField(max_length=100)

class EditQuery(models.Model):
    query = models.CharField(max_length=20000)
