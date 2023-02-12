from django.core.mail import EmailMessage
from register_events.models import Participant
from register_events.views.views_pdf import create_pdf

def send_certificate_to_participant(participant: Participant):
    '''Envia email com certificado em anexo'''
    email = EmailMessage(
        subject='Seu certificado!',
        body=f'Olá, { participant.name }. Seu certificado encontra-se em anexo.',
        from_email='Equipe Seu Evento <oi@seuevento.com>',
        to=[participant.email],
        reply_to=['<oi@seuevento.com'],
    )
    events = participant.events.all()
    for event in events:
        pdf = create_pdf(event, participant)
        email.attach(f'{ event.name }.pdf', pdf.read(), 'application/pdf')
    email.send()