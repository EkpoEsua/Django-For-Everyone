from django.db import models
from django.db.models.deletion import CASCADE, SET, SET_NULL

# Create your models here.

class Site(models.Model):
    
    name = models.CharField(max_length=200, null=False, unique=True)
    description = models.TextField()
    justification = models.TextField()
    year = models.IntegerField(null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area_hectares = models.FloatField(null=True)
    category = models.ForeignKey('Category', on_delete=SET_NULL, null=True)
    state = models.ForeignKey('State', on_delete=SET_NULL, null=True)
    region = models.ForeignKey('Region', on_delete=SET_NULL, null=True)
    iso = models.ForeignKey('Iso', on_delete=SET_NULL, null=True)


class Region(models.Model):

    name = models.CharField(max_length=200)


class State(models.Model):

    name = models.CharField(max_length=200)

class Iso(models.Model):

    name = models.CharField(max_length=2)

class Category(models.Model):

    name = models.CharField(max_length=200)



