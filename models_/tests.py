from django.test import TestCase

from models_.models import Person, PersonLocation


def create_person(name, lon, lat, masl):
    p = Person.objects.create(name=name)
    PersonLocation.objects.create(person=p, lon=lon, lat=lat, masl=masl)


class ModelsTest(TestCase):
    def test_person_locations(self):
        person_test_data = [
            ['Alex', 51.2143, 48.0184, 157],
            ['Fred', 80.116, 31.16, 234],
            ['Johnny', 68.186, 11.849, 1008],
            ['Victor', 29.1981, 78.116, 20],
        ]
        for person in person_test_data:
            create_person(*person)

        print(Person.objects.all())
        print(Person.objects.all()[0].location)