from django.db import models

class MyQuery(models.Model):
    user = models.CharField(max_length=100)    
    query = models.CharField(max_length=10000)
    
    def __str__(self):
        return self.query
    def __unicode__(self):
        return self.query

class Login(models.Model):
    user = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
