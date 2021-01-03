from django.contrib import admin
from .models import Person, Event, Comment


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('initiator', 'location', 'base', 'check_out', 'check_out', 'buddy', 'complete')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('edipi','rank','lname','fname')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
