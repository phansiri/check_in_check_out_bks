from django.contrib import admin
from .models import Person, Event, Comment

admin.site.register(Person)
admin.site.register(Event)
admin.site.register(Comment)