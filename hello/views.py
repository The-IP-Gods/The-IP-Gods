from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, AppNums, Keywords

from .forms import NameForm

import csv
import sys

# Create your views here.
def index(request):
    results = []
    csv.field_size_limit(sys.maxsize)
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid() and form.cleaned_data['your_name'] != "":
            reader = csv.reader(open('hello/static/supertable.copied'))
            for line in reader:
                if line[0] == form.cleaned_data['your_name']:
                    if form.cleaned_data['email'] != "":
                        AppNums.objects.create(email=form.cleaned_data['email'], appnums=form.cleaned_data['your_name']).save()
                    results.append(line)
            return render(request, 'index.html', {'results': results})
        elif form.is_valid and form.cleaned_data['keywords'] != "":
            if form.cleaned_data['email'] != "":
                Keywords.objects.create(email=form.cleaned_data['email'], keywords=form.cleaned_data['keywords']).save()
            superreader = csv.reader(open('hello/static/supertable.copied'))
            for line in superreader:
                if form.cleaned_data['keywords'] in line[3]:
                    results.append(line)
            return render(request, 'index.html', {'results': results})
    else:
        form = NameForm()
    return render(request, 'index.html', {'form': form})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def form(request):
    results = []
    csv.field_size_limit(sys.maxsize)
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid() and form.cleaned_data['your_name'] != "":
            reader = csv.reader(open('hello/static/ipgod107.csv'))
            for line in reader:
                if line[0] == form.cleaned_data['your_name']:
                    if form.cleaned_data['email'] != "":
                        AppNums.objects.create(email=form.cleaned_data['email'], appnums=form.cleaned_data['your_name']).save()
                        return HttpResponse('The status of application '+line[0]+' is '+line[9]+'. You will receive updates at your email address, '+form.cleaned_data['email'])
                    return HttpResponse('The status of application '+line[0]+' is '+line[9])
            return HttpResponse('Sorry, but we couldn\'t find that application number in our database.')
        elif form.is_valid and form.cleaned_data['keywords'] != "":
            if form.cleaned_data['email'] != "":
                Keywords.objects.create(email=form.cleaned_data['email'], keywords=form.cleaned_data['keywords']).save()
            reader122a = csv.reader(open('hello/static/supertable.copied'))
            for line in reader122a:
                if form.cleaned_data['keywords'] in line[1]:
                    reader107 = csv.reader(open('hello/static/ipgod107.csv'))
                    for line107 in reader107:
                        if line[0] == line107[0]:
                            status = line107[9]
                            category = line107[6]
                    results.append((line[0],line[1],line107[9],line107[6]))
            return render(request, 'results.html', {'results': results})
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

def team(request):
    return render(request, 'team.html')
