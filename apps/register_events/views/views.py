from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from register_events.forms import ParticipantForms
from register_events.models import Event, Participant
from register_events.utils import available_events


@login_required(login_url='/admin/login/')
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


@login_required(login_url='/admin/login/')
def submit_partipant_form(request, participant_id):
    '''Submissão da participação'''
    participant = get_object_or_404(Participant, id=participant_id)
    event_id = request.POST.get('event')
    participant.events.add(Event.objects.get(id=event_id))
    participant.save()
    return JsonResponse({'message': 'ok'})


@login_required(login_url='/admin/login/')
def view_register_success(request):
    '''Sucesso ao registrar participante'''
    context = {'page_title': 'Sucesso'}
    return render(request, 'register_events/success.html', context)


@login_required(login_url='/admin/login/')
def view_register_error(request):
    '''Erro ao registrar participante'''
    context = {'page_title': 'Erro'}
    return render(request, 'register_events/error.html', context)