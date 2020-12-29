from django.test import TestCase
from cico_app.models import Person, Event


class PersonTest(TestCase):
    def setUp(self) -> None:
        rank, lname, fname, branch, category, edipi, phone = 'SGT', 'Smith', 'Joe', 'USMC', \
                                                             'Active Duty member', '1234567898', '08075432334'
        Person.objects.create(rank=rank, lname=lname, fname=fname, branch=branch,
                              category=category, edipi=edipi, phone=phone)

    def test_person_rank(self):
        person = Person.objects.get(edipi='1234567898')
        self.assertEqual(person.rank, 'SGT')

    def test_person_lname(self):
        person = Person.objects.get(edipi='1234567898')
        self.assertEqual(person.lname, 'Smith')

    def test_person_fname(self):
        person = Person.objects.get(edipi='1234567898')
        self.assertEqual(person.fname, 'Joe')

    def test_person_branch(self):
        person = Person.objects.get(edipi='1234567898')
        self.assertEqual(person.branch, 'USMC')

    def test_person_category(self):
        person = Person.objects.get(edipi='1234567898')
        self.assertEqual(person.category, 'Active Duty member')

    def test_person_edipi(self):
        person = Person.objects.get(edipi='1234567898')
        self.assertEqual(person.edipi, '1234567898')

    def test_person_phone(self):
        person = Person.objects.get(edipi='1234567898')
        self.assertEqual(person.phone, '08075432334')

    def test_to_string(self):
        person = Person.objects.get(edipi='1234567898')
        self.assertEqual(str(person), 'SGT Smith, Joe')

class EventTest(TestCase):
    def setUp(self) -> None:
        rank, lname, fname, branch, category, edipi, phone = 'SGT', 'Smith', 'Joe', 'USMC', \
                                                             'Active Duty member', '1234567898', '08075432334'
        Person.objects.create(rank=rank, lname=lname, fname=fname, branch=branch,
                              category=category, edipi=edipi, phone=phone)
        initiator = Person.objects.get(edipi=1234567898)
