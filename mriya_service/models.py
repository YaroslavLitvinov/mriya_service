from django.db import models

class Login(models.Model):
    user = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
    
class EditQuery(models.Model):
    query = models.CharField(max_length=20000)
