from django.contrib import admin
from django.conf.locale.pt_BR import formats as portuguese
from django.conf.locale.en import formats as english
from .models import Event, Participant

portuguese.DATE_FORMAT = 'd/m/Y'
portuguese.DATETIME_FORMAT = 'H:i - d/m/Y'
english.DATE_FORMAT = 'd/m/Y'
english.DATETIME_FORMAT = 'H:i - d/m/Y'


@admin.register(Event)
class EventRegister(admin.ModelAdmin):
    list_display = ['id', 'name', 'date', 'is_active', 'participants_count']
    list_display_links = ['id', 'name']
    list_editable = ['is_active']
    ordering = ['id']
    readonly_fields = ['id']
    search_fields = ['name',]

    def participants_count(self, obj):
        return obj.event_participants.count()
    participants_count.short_description = 'Participants'


@admin.register(Participant)
class ParticipantRegister(admin.ModelAdmin):
    change_form_template = 'register_events/admin_participant_changeform.html'

    autocomplete_fields = ['events']
    list_display = ['id', 'name', 'email', 'birth_date', 'events_count']
    list_display_links = ['id', 'name']
    ordering = ['id']
    readonly_fields = ['id']
    search_fields = ['name', 'email']

    def events_count(self, obj):
        return obj.events.all().count()
    events_count.short_description = 'Events'
