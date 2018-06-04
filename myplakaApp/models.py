from __future__ import unicode_literals
from django.conf import settings
from django.db import models
# Create your models here.
class Search(models.Model):
    plaka=models.CharField(max_length=8)
    owner=models.CharField(max_length=20)
    phone=models.CharField(max_length=11)
    date=models.DateTimeField()
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.plaka

""" class Bildirim(models.Model):
    notification=models.ForeignKey('myplakaApp.Search',related_name='bildirim', on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    content=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
"""