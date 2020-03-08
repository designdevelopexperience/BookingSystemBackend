from rest_framework import serializers

from .models import Owner, Event


class OwnerSerializer(serializers.ModelSerializer):
    events = serializers.StringRelatedField(many=True)

    class Meta:
        model = Owner
        fields = ['id', 'first_name', 'last_name', 'events']


class EventSerializer(serializers.ModelSerializer):
    enrollments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Event
        fields = ['id', 'event_name', 'date', 'capacity', 'enrollments']
