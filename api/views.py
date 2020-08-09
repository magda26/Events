from django.shortcuts import render

from rest_framework import viewsets

from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('created_date')
    serializer_class = EventSerializer
    detail_serializer_class = DetailEventSerializer
    http_method_names = ['get']


    def get_serializer_class(self):
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class
        return self.serializer_class
