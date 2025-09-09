from rest_framework import viewsets
from .models import Center, Employee, Telescope, Event
from .serializers import CenterSerializer, EmployeeSerializer, TelescopeSerializer, EventSerializer

class CenterViewSet(viewsets.ModelViewSet):
    """
    API Center
    """
    queryset = Center.objects.all()
    serializer_class = CenterSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API Employee
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class TelescopeViewSet(viewsets.ModelViewSet):
    """
    API Telescope
    """
    queryset = Telescope.objects.all()
    serializer_class = TelescopeSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    API Event
    """
    queryset = Event.objects.all().order_by('-observation_date')
    serializer_class = EventSerializer
