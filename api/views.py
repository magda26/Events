from django.shortcuts import render

from rest_framework import viewsets

from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('created_date')
    serializer_class = EventSerializer
    http_method_names = ['get']

