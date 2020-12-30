from django.test import TestCase
from cico_app.models import Person, Event
from cico_app.forms import EventForm, PersonForm
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect

from urllib.parse import urlencode


# from django.core.urlresolvers import reverse


class EventTest(TestCase):
    def setUp(self) -> None:
        rank, lname, fname, branch, category, edipi, phone = 'SGT', 'Smith', 'Joe', 'USMC', \
                                                             'Active Duty member', '1234567898', '08075432334'
        Person.objects.create(rank=rank, lname=lname, fname=fname, branch=branch,
                              category=category, edipi=edipi, phone=phone)
        initiator = Person.objects.get(edipi=1234567898)
        check_out = timezone.now()
        check_in = timezone.now()
        Event.objects.create(initiator=initiator, check_out=check_out, check_in=check_in, location='PX',
                             buddy='Mike Jones', complete=True)

    def test_event_list(self):
        url = reverse('event_list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_event_new(self):
        person = Person.objects.get(edipi=1234567898)
        url = reverse('event_new', args=[person.pk])
        resp = self.client.get(url)
        self.assertEqual(url, f'/event/new/{person.pk}')
        self.assertEqual(resp.status_code, 200)

    def test_person_list(self):
        url = reverse('person_list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_person_new(self):
        person = Person.objects.get(edipi=1234567898)
        url = reverse('person_edit', args=[person.pk])
        resp = self.client.get(url)
        self.assertEqual(url, f'/person/{person.pk}/edit')
        self.assertEqual(resp.status_code, 200)

    def test_scan(self):
        url = reverse('scan')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)





