# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Department(models.Model):
    DEPARTMENT_CHOICES = (
        ('TE', 'TELUGU'),
        ('EN', 'ENGLISH'),
        ('MA', 'MATHS'),
        ('PH', 'PHYSICS'),
        ('CS', 'COMPUTERS'),
    )
    department_name = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)

    objects = models.Manager()


class StudentApplication(TimeStampModel):
    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()
    ssc_doc = models.FileField(upload_to='documents/ssc/')
    inter_doc = models.FileField(upload_to='documents/inter/')
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.student_name

    objects = models.Manager()


class StudentRegistration(TimeStampModel):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    application = models.OneToOneField(StudentApplication, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='student/images/')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None)
    nationality = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.user.username

class StaffRegistration(TimeStampModel):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None)
    age = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    profile_pic = models.ImageField(upload_to='staff/images/')
    nationality = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.user.username
