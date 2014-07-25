from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Location(models.Model):
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=8, decimal_places=6)
    masl = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return 'longitude: %s, latitude: %s, masl: %s' % (self.lon, self.lat, self.masl)


class PersonLocation(Location):
    person = models.OneToOneField(Person, related_name='location')


class BuildingLocation(Location):
    building = models.ForeignKey(Building, related_name='location')