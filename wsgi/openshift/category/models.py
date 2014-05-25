from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Hello(CMSPlugin):
    guest_name = models.CharField(max_length=50, default='Guest')
