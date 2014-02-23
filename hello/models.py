from django.db import models
from cms.models.pluginmodel import CMSPlugin

# Create your models here.

class Hello(CMSPlugin):
    guest_name = models.CharField(max_length=50, default='Guest')
