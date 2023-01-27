import datetime, qrcode, socket
from django.db.models import QuerySet
from .models import Event


def available_events() -> QuerySet:
    '''Retorna eventos disponíveis hoje'''
    today = datetime.datetime.now()
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)
    tomorrow = today + datetime.timedelta(days=1)
    events = Event.objects.filter(
        date__range=(today, tomorrow),
        is_active=True
    )
    return events


def get_ip_address():
    '''Return IP adress'''
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


def generate_participant_qrcode(participant_id):
    '''Cria QR Code para participante'''
    site_url = f'http://{ get_ip_address() }:8000'
    # site_url = f'https://you-site-domain'
    img = qrcode.make(f'{ site_url }/register_events/register_participant?participant={ participant_id }')
    return img