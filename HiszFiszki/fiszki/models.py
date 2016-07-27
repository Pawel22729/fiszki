from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Words(models.Model):
    word = models.CharField(max_length=15)
    trans = models.CharField(max_length=15)
    counter = models.CharField(max_length=100, default='0')