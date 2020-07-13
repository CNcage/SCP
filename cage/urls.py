from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:scp_id>/", views.detail, name="detail"),
    path("locations/", views.place, name="locations"),
    # path("locations/sightings/", views.sightings, name="sightings"),
    path("locations/sightings/<int:location_id>/", views.sightings, name="sightings"),
]