# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # "user_%d" % instance.owner.id, "car_%s" % instance.slug, filename
    return 'user_{0}/{1}'.format(instance.email, filename)


class Student(models.Model):
    name = models.CharField(max_length=100)
    DOB = models.DateField(default='1996-02-11')
    email = models.EmailField(max_length=100)
    mobile = models.CharField(default="0", max_length=10)
    marks = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return self.name + str(self.pk)
