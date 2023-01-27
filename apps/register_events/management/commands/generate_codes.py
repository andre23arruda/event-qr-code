import qrcode, socket
from django.core.management.base import BaseCommand
from register_events.models import Participant


def get_ip_address():
    '''Return IP adress'''
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def generate_codes():
    '''Cria QR Code para cada participante'''
    site_url = f'http://{ get_ip_address() }:8000'
    # site_url = f'https://you-site-domain'

    participants = Participant.objects.all()
    for participant in participants:
        img = qrcode.make(f'{ site_url }/register_events/register_participant?participant={ participant.id }')
        img.save(f'./qr_codes/code-{ participant.id }.png')
    print('Sucesso!')


class Command(BaseCommand):
    help = 'Generate codes'

    def handle(self, *args, **options):
        generate_codes()