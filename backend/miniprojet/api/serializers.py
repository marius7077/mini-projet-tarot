from rest_framework import serializers
from .models import Center, Employee, Telescope, Event

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'role', 'center']

class TelescopeSerializer(serializers.ModelSerializer):
    center = serializers.StringRelatedField()  # Affiche le nom du centre au lieu de l'ID

    class Meta:
        model = Telescope
        fields = ['id', 'name', 'location', 'latitude', 'longitude', 'description', 'center']

class EventSerializer(serializers.ModelSerializer):
    telescope = TelescopeSerializer(read_only=True)

    class Meta:
        model = Event
        fields = [
            'id',
            'name',
            'event_type',
            'discovery_date',
            'observation_date',
            'description',
            'duration_minutes',
            'telescope'
        ]

class CenterSerializer(serializers.ModelSerializer):
    telescopes = TelescopeSerializer(many=True, read_only=True)
    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Center
        fields = ['id', 'name', 'location', 'description', 'telescopes', 'employees']
