from django.db import models

class Center(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    center = models.ForeignKey(Center, on_delete=models.CASCADE, related_name='employees')
    role = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Telescope(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    center = models.ForeignKey(Center, on_delete=models.CASCADE, related_name='telescopes')

    def __str__(self):
        return self.name

class Event(models.Model):
    EVENT_TYPES = [
        ('GRB', 'Gamma Ray Burst'),
        ('SN', 'Supernova'),
        ('GW', 'Gravitational Wave'),
        ('NU', 'Neutrino'),
    ]
    name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=10, choices=EVENT_TYPES)
    discovery_date = models.DateField(blank=True, null=True, help_text="Date de découverte de l'événement")
    observation_date = models.DateTimeField(blank=True, null=True, help_text="Date d'observation par le télescope")
    description = models.TextField()
    duration_minutes = models.IntegerField(blank=True, null=True)
    telescope = models.ForeignKey(Telescope, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return f"{self.name} ({self.get_event_type_display()})"
