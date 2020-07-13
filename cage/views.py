from django.shortcuts import render, redirect
from .models import Monster
from .models import Location
from django.http import HttpResponse

def index(request):
    context = {"monsters": Monster.objects.all()}
    return render (request, "cage/index.html", context)

def detail(request, scp_id):
    context = {"monster": Monster.objects.get(pk=scp_id)}
    return render (request, "cage/profile.html", context)

def place(request):
    context = {"locations": Location.objects.all()}
    return render (request, "cage/locations.html", context)

def sightings(request, location_id):
    l = Location.objects.get(pk=location_id)
    monsters = Monster.objects.filter(location=l)
    context = {"monsters": monsters}
    return render (request, "cage/sightings.html", context)
    # print(context)

# return HttpResponse(m.monster_name)
