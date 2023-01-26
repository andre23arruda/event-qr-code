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
    list_display = ['id', 'name', 'date', 'is_active']
    list_display_links = ['id', 'name']
    list_editable = ['is_active']
    ordering = ['id']
    search_fields = ['name',]


@admin.register(Participant)
class ParticipantRegister(admin.ModelAdmin):
    autocomplete_fields = ['events']
    list_display = ['id', 'name', 'email', 'birth_date', 'events_count']
    list_display_links = ['id', 'name']
    ordering = ['id']
    search_fields = ['name', 'email']

    def events_count(self, obj):
        return obj.events.all().count()
    events_count.short_description = 'Events'
