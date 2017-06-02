from django.db import models
from elfinder.fields import ElfinderField

class MyQuery(models.Model):
    user = models.CharField(max_length=130, unique=True)
    filename = ElfinderField()
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

class FMTestModel(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    anyfile = ElfinderField()
    image = ElfinderField(optionset='user_files')
    
    def __unicode__(self):
        return self.name    
