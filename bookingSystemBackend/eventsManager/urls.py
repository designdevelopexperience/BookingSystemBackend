from django.urls import path
from .views import events_list, enrollments_list

urlpatterns = [
    path('events', events_list, name="events_list"),
    path('enrollments', enrollments_list, name="enrollments_list"),
]