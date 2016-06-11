from __future__ import unicode_literals

from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=13)
    email = models.EmailField()
    work_experience = models.FloatField()
    analytics_experience = models.FloatField()
    current_location = models.CharField(max_length=15)
    corrected_location = models.CharField(max_length=15)
    nearest_city = models.CharField(max_length=15)
    prefered_location = models.CharField(max_length=15)
    ctc = models.FloatField()
    designation = models.CharField(max_length=50)
    skills = models.ForeignKey('Skill')


class Skill(models.Model):
    name = models.CharField(max_length=15)
