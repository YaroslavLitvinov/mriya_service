from django.db import models

class MyQuery(models.Model):
    user = models.CharField(max_length=130, unique=True)
    query = models.CharField(max_length=10000)
    src = models.CharField(max_length=100)
    dst = models.CharField(max_length=100)    
    
    def __str__(self):
        return self.query
    def __unicode__(self):
        return self.query

class Config(models.Model):
    user = models.CharField(max_length=130, unique=True)
    config = models.CharField(max_length=1000)
