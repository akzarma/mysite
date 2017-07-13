# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # "user_%d" % instance.owner.id, "car_%s" % instance.slug, filename
    return 'user_{0}/{1}'.format(instance.gr_number, filename)


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    DOB = models.DateField(default='1996-02-11')
    admission_type = models.CharField(max_length=50)
    shift = models.CharField(max_length=1)
    caste_type = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
    gr_number = models.CharField(max_length=15)

    # personal details
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField(default="0", max_length=10)
    religion = models.CharField(max_length=20)
    sub_caste = models.CharField(max_length=30)
    handicapped = models.BooleanField(default=0)
    nationality = models.CharField(max_length=50)

    # emergency contact
    emergency_name = models.CharField(max_length=50)
    emergency_mobile = models.BigIntegerField(max_length=10)
    emergency_relation = models.CharField(max_length=50)
    emergency_address = models.CharField(max_length=100)

    # family
    # father
    father_name = models.CharField(max_length=50)
    father_profession = models.CharField(max_length=30)
    father_designation = models.CharField(max_length=30)
    father_mobile = models.BigIntegerField()
    father_email = models.EmailField()
    # mother
    mother_name = models.CharField(max_length=50)
    mother_profession = models.CharField(max_length=30)
    mother_designation = models.CharField(max_length=30)
    mother_mobile = models.BigIntegerField()
    mother_email = models.EmailField()

    # permanent address
    permanent_address = models.CharField(max_length=100)
    permanent_state = models.CharField(max_length=50)
    permanent_city = models.CharField(max_length=50)
    permanent_pin_code = models.IntegerField()
    permanent_country = models.CharField(max_length=50)

    # current address
    current_address = models.CharField(max_length=100)
    current_state = models.CharField(max_length=50)
    current_city = models.CharField(max_length=50)
    current_pin_code = models.IntegerField()
    current_country = models.CharField(max_length=50)

    # Exam details
    jee_physics = models.IntegerField()
    jee_maths = models.IntegerField()
    jee_chemistry = models.IntegerField()
    jee_total = models.IntegerField()
    jee_max_physics = models.IntegerField()
    jee_max_maths = models.IntegerField()
    jee_max_chemistry = models.IntegerField()

    # documents
    doc_tenth_marksheet = models.FileField(upload_to=user_directory_path)
    doc_twelfth_marksheet = models.FileField(upload_to=user_directory_path)
    doc_jee_marksheet = models.FileField(upload_to=user_directory_path)
    doc_profile_pic = models.FileField()

    def __str__(self):
        return self.first_name + ' ' + str(self.pk)
