import os
import sys
import django
import random
from datetime import datetime, timedelta

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "miniprojet.settings")
django.setup()

from api.models import Center, Telescope, Employee, Event

print("Suppression des données")
Event.objects.all().delete()
Telescope.objects.all().delete()
Employee.objects.all().delete()
Center.objects.all().delete()

print("Création des centres")
centers_data = [
    {"name": "Centre de Paris", "location": "Paris", "description": "Centre principal en France"},
    {"name": "Centre de La Réunion", "location": "La Réunion", "description": "Observatoire de l'île"},
    {"name": "Centre du Chili", "location": "Chili", "description": "Observatoire sud-américain"}
]

centers = []
for data in centers_data:
    center = Center.objects.create(**data)
    centers.append(center)

print("Création des télescopes")
telescope_names = ["TAROT-1", "TAROT-2", "TAROT-3", "TAROT-4"]
for center in centers:
    for i in range(2):  # 2 télescopes par centre
        Telescope.objects.create(
            name=f"{telescope_names[i]} ({center.location})",
            location=center.location,
            latitude=random.uniform(-90, 90),
            longitude=random.uniform(-180, 180),
            description=f"Télescope du {center.name}",
            center=center
        )

print("Création des employés")
roles = ["Astronome", "Technicien", "Ingénieur", "Doctorant"]
for center in centers:
    for i in range(3):  # 3 employés par centre
        Employee.objects.create(
            first_name=f"Prenom{i+1}",
            last_name=f"Nom{i+1}",
            email=f"user{i+1}_{center.name.replace(' ', '').lower()}@example.com",
            role=random.choice(roles),
            center=center
        )

print("Création des événements")
event_types = ["GRB", "SN", "GW", "NU"]
for telescope in Telescope.objects.all():
    for i in range(3):  # 3 événements par télescope
        Event.objects.create(
            name=f"Event {i+1} ({telescope.name})",
            event_type=random.choice(event_types),
            discovery_date=datetime.now().date() - timedelta(days=random.randint(1, 100)),
            observation_date=datetime.now() - timedelta(days=random.randint(0, 100), hours=random.randint(0, 23)),
            description=f"Observation simulée de {telescope.name}",
            duration_minutes=random.randint(10, 120),
            telescope=telescope
        )

print("Données de test créées avec succès !")
