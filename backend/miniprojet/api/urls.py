from django.urls import path, include
from rest_framework import routers
from .views import CenterViewSet, EmployeeViewSet, TelescopeViewSet, EventViewSet

router = routers.DefaultRouter()
router.register(r'telescopes', TelescopeViewSet)
router.register(r'events', EventViewSet)
router.register(r'centers', CenterViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]