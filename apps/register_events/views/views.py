import base64, io, urllib
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from register_events.forms import ParticipantForms
from register_events.models import Event, Participant
from register_events.utils import available_events, generate_participant_qrcode


@login_required(redirect_field_name='next', login_url='/admin/login/')
def participant_form(request):
    '''Página com formulário de participação do evento'''
    participant_id = request.GET.get('participant')
    participant = get_object_or_404(Participant, id=participant_id)
    # has_events = available_events()
    has_events = True

    if has_events:
        context = {
            'page_title': 'Registrar Participante em Evento',
            'form': ParticipantForms(instance=participant),
            'participant_id': participant_id,
            'has_events': has_events
        }
        return render(request, 'register_events/index.html', context)

    return render(request, 'register_events/no-events.html')


@login_required(redirect_field_name='next', login_url='/admin/login/')
def submit_participant_form(request, participant_id):
    '''Submissão da participação'''
    participant = get_object_or_404(Participant, id=participant_id)
    event_id = request.POST.get('event')
    participant.events.add(Event.objects.get(id=event_id))
    participant.save()
    return JsonResponse({'message': 'ok'})


@login_required(redirect_field_name='next', login_url='/admin/login/')
def success_participant_form(request):
    '''Sucesso ao registrar participante'''
    context = {'page_title': 'Sucesso'}
    return render(request, 'register_events/success.html', context)


@login_required(redirect_field_name='next', login_url='/admin/login/')
def error_participant_form(request):
    '''Erro ao registrar participante'''
    context = {'page_title': 'Erro'}
    return render(request, 'register_events/error.html', context)


@login_required(redirect_field_name='next', login_url='/admin/login/')
def see_qrcode(request, participant_id):
    '''Exibe qr code do participante'''
    participant = get_object_or_404(Participant, pk=participant_id)
    img = generate_participant_qrcode(participant_id)
    buf = io.BytesIO()
    img.save(buf, 'PNG')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    context = {
        'img_b64': uri,
        'participant': participant,
        'page_title': f'QR Code: { participant.name }'
    }
    return render(request, 'register_events/see_qrcode.html', context)