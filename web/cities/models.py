from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    home_town = models.CharField(max_length=25)


class Phone(models.Model):
    company = models.CharField(max_length=25)
    series = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    available = models.BooleanField()
    count = models.IntegerField()
