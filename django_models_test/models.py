from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=20)


class Person(models.Model):
    name = models.CharField(max_length=20)


class Location(models.Model):
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=8, decimal_places=6)
    masl = models.DecimalField(max_digits=8, decimal_places=2)
    person = models.OneToOneField(Person)
    building = models.ForeignKey(Building)