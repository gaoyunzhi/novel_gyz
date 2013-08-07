from django.db import models
from django.forms.models import model_to_dict

# Create your models here.

class NovelRequests(models.Model):
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    email = models.EmailField(max_length=254) # for 254, see django documents
    filename = models.CharField(max_length=200) # may change later to FileField
    def __unicode__(self):
        return str(model_to_dict(self))
    

class NovelAchieved(models.Model):
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    filename = models.CharField(max_length=200)
    def __unicode__(self):
        return str(model_to_dict(self))
    
