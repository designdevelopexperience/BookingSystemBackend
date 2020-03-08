from django.http import HttpResponse, JsonResponse
from .models import Event, Enrollment


def events_list(request):
    max_objects = 20
    events = Event.objects.all()[:max_objects]
    data = {"results": list(events.values("owner_id", "event_name", "date", "capacity"))}
    # data = {"results": {
    #     "events": events.values,
    # }}
    return JsonResponse(data)


def enrollments_list(request):
    max_objects = 20
    polls = Enrollment.objects.all()[:max_objects]
    data = {"results": list(polls.values("client__enrollment__event_id", "event__enrollment__client_id"))}
    return JsonResponse(data)