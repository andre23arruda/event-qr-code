import datetime
from django.db.models import QuerySet
from .models import Event


def available_events() -> QuerySet:
    '''Retorna eventos disponíveis hoje'''
    today = datetime.datetime.now()
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)
    tomorrow = today + datetime.timedelta(1)
    events = Event.objects.filter(
        date__range=(today, tomorrow),
        is_active=True
    )
    return events
