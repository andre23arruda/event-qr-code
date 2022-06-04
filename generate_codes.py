import django, os, qrcode

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()


def create_codes():
    '''Criando pessoas para nosso banco de dados'''
    from register_events.models import Participant
    from setup.env import get_ip_address

    site_url = f'http://{ get_ip_address() }:8000'
    # site_url = f'https://you-site-domain'

    participants = Participant.objects.all()
    for participant in participants:
        img = qrcode.make(f'{ site_url }/register_events/register_participant?participant={ participant.id }')
        img.save(f'./qr_codes/code-{ participant.id }.png')

create_codes()
print('Sucesso!')
