from django.shortcuts import render
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from rest_framework.response import Response

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    http_method_names = ['get','post','put','delete']

    def list(self, request):
        queryset = Event.objects.all().filter(user=request.user).order_by('-creation_date')
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        event = self.get_object()
        serializer = EventSerializer(event)
        event.delete()
        return Response(serializer.data)


def index(request):
    return render(request, "events/index.html")
