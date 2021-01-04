from django.db import models
from django.utils import timezone


class Person(models.Model):
    NONE = '-'
    ALPHA = 'A'
    BRAVO = 'B'
    DCO = 'DCO'
    HEADQUARTERS = 'HQ'
    SERVICE = 'SVC'
    COMPANY_CHOICES = [
        (NONE, '---'),
        (ALPHA, 'Alpha'),
        (BRAVO, 'Bravo'),
        (DCO, 'DCO-IDM'),
        (HEADQUARTERS, 'Headquarters'),
        (SERVICE, 'Service'),
    ]
    rank = models.CharField(max_length=7)
    lname = models.CharField(max_length=27)
    fname = models.CharField(max_length=21)
    branch = models.CharField(max_length=10)
    category = models.CharField(max_length=30)
    edipi = models.CharField(max_length=11)
    phone = models.CharField(max_length=20, null=True, blank=True)
    company_in_battalion = models.CharField(max_length=3, choices=COMPANY_CHOICES, default=NONE)

    def __str__(self):
        return f'{self.rank} {self.lname}, {self.fname}'


class Event(models.Model):
    initiator = models.ForeignKey(Person, on_delete=models.CASCADE)
    check_out = models.DateTimeField()
    check_in = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=300)
    base = models.BooleanField(default=False)
    buddy = models.CharField(max_length=100, null=True, blank=True)
    complete = models.BooleanField(default=False)

    def complete_event(self):
        self.check_in = timezone.localtime(timezone.now())
        self.complete = True
        self.save()

    def __str__(self):
        return f'Initiator: {self.initiator}'


class Scanner(models.Model):
    barcode = models.CharField(max_length=90)


class Comment(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
