from rest_framework import viewsets

from .serializers import OwnerSerializer, EventSerializer
from .models import Owner, Event


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all().order_by('first_name')
    serializer_class = OwnerSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('event_name')
    serializer_class = EventSerializer