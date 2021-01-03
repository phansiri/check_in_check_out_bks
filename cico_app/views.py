from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import Person, Event
from .forms import EventForm, PersonForm
from cac_parser import PDF417Barcode


def event_list(request):
    events = Event.objects.all().order_by('-check_in')
    context = {
        'events': events,
    }
    return render(request, 'cico_app/event_list.html', context)


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    context = {
        'event': event
    }
    return render(request, 'cico_app/event_detail.html', context)


def event_new(request, pk=None):
    person: Person = None
    if pk:
        person = Person.objects.get(pk=pk)
    form = EventForm()
    context = {
        'person': person,
        'form': form,
    }
    if request.method.lower() == 'post':
        form = EventForm(request.POST)
        flag: bool

        if form.is_valid():
            event = form.save(commit=False)
            event.initiator = person
            event.location = request.POST['location']

            event.buddy = request.POST['buddy']
            if 'base' in request.POST.keys():
                flag = True
            else:
                flag = False
            event.base = flag
            event.check_out = timezone.localtime(timezone.now())
            event.save()
        return redirect('event_list')

    return render(request, 'cico_app/event_new.html', context)


def event_edit(request, pk=None):
    pass


def person_list(request):
    persons = Person.objects.all()
    context = {
        'persons': persons,
    }
    return render(request, 'cico_app/person_list.html', context)


def person_edit(request, pk=None):
    person = get_object_or_404(Person, pk=pk)
    if request.method.lower() == 'post':

        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            person.phone = request.POST['phone']
            person.save()
            context = {
                'person': person.pk
            }
            return HttpResponseRedirect(reverse('event_new', args=(person.pk,)))
    form = PersonForm(instance=person)
    context = {
        'form': form,
        'person': person,
    }
    return render(request, 'cico_app/person_edit.html', context)


def scan(request):
    if request.method.lower() == 'post':
        barcode = request.POST.get('scanner')
        item = PDF417Barcode(barcode)  # parse cac for vital information
        person: Person = None
        try:
            person = Person.objects.get(edipi=item.edipi)
        except:
            pass

        if not person:  # person doesn't exist
            person = Person.objects.create(
                rank=item.rank,
                lname=item.lname,
                fname=item.fname,
                branch=item.branch,
                category=item.category,
                edipi=item.edipi,
            )
            return HttpResponseRedirect(reverse('person_edit', args=(person.pk,)))
        else:  # person exists
            events = Event.objects.all()
            # checks if events exists
            if events.filter(initiator=person).exists():
                # check if there is an event that is false...
                if events.filter(initiator=person, complete=False).exists():
                    print('Inside the complete false if it exists')
                    event = events.filter(initiator=person).get(complete=False)
                    event.complete_event()
                    return redirect('event_list')
                else:
                    print('Inside the complete true if it exists')
                    # needs to redirect to event creation
                    return HttpResponseRedirect(reverse('person_edit', args=(person.pk,)))
            else:
                # person exists but has no events
                return HttpResponseRedirect(reverse('person_edit', args=(person.pk,)))

    context = {
        'form': None,
    }
    return render(request, 'cico_app/event_list.html', context)


def reports(request):
    context = {
        'test': 'test',
    }
    return render(request, 'cico_app/reports.html', context)