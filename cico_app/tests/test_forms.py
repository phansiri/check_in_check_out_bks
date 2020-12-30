from django.test import TestCase
from cico_app.models import Person, Event, Scanner
from django.utils import timezone
from cico_app.forms import PersonForm, EventForm, ScannerForm


class PersonFormTest(TestCase):
    def setUp(self) -> None:
        rank, lname, fname, branch, category, edipi, phone = 'SGT', 'Smith', 'Joe', 'USMC', \
                                                             'Active Duty member', '1234567898', '08075432334'
        Person.objects.create(rank=rank, lname=lname, fname=fname, branch=branch,
                              category=category, edipi=edipi, phone=phone)

    def test_person_valid_form(self):
        data = {
            'rank': 'SGT',
            'lname': 'Smith',
            'fname': 'Joe',
            'branch': 'USMC',
            'category': 'Active Duty member',
            'edipi': '1234567898',
            'phone': '08075432334',
        }
        form = PersonForm(data=data)
        self.assertTrue(form.is_valid())

    def test_person_invalid_form(self):
        data = {
            'rank': 'SGT',
            'lname': 'Smith',
            'fname': 'Joe',
            'branch': 'USMC',
            'category': '',
            'edipi': '1234567898',
            'phone': '08075432334',
        }
        form = PersonForm(data=data)
        self.assertFalse(form.is_valid())

    def test_event_valid_form(self):
        check_out = timezone.now()
        check_in = timezone.now()
        person = Person.objects.get(edipi=1234567898)
        data = {
            'initiator': person,
            'location': 'Outside',
            'check_out': check_out,
            'check_in': check_in,
            'buddy': 'Superman',
            'complete': True
        }
        form = EventForm(data)
        self.assertTrue(form.is_valid())

    def test_event_invalid_form(self):
        check_out = timezone.now()
        check_in = timezone.now()
        person = Person.objects.get(edipi=1234567898)
        data = {
            'initiator': person,
            'location': '',
            'check_out': check_out,
            'check_in': check_in,
            'buddy': 'Superman',
        }
        form = EventForm(data)
        self.assertFalse(form.is_valid())
