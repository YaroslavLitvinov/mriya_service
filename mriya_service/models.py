from django.db import models

class MyQuery(models.Model):
    user = models.CharField(max_length=100, unique=True)
    query = models.CharField(max_length=10000)
    
    def __str__(self):
        return self.query
    def __unicode__(self):
        return self.query
