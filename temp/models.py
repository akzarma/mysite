# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    DOB = models.DateField(default='1996-02-11')
    email = models.EmailField(max_length=100)
    mobile = models.CharField(default="0",max_length=10)
    marks = models.FileField(upload_to='temp/media/documents/1/')
    def __str__(self):
        return self.name + str(self.pk)