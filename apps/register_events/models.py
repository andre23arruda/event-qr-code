from django.db import models
from django.utils.translation import ugettext_lazy as _
from shortuuid.django_fields import ShortUUIDField


class Event(models.Model):
    id = ShortUUIDField(length=8, primary_key=True)
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateField(auto_now=True, verbose_name=_('Updated at'))
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    taught_by = models.CharField(max_length=20, verbose_name=_('Taught by'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    date = models.DateTimeField(verbose_name=_('Date'))
    how_long = models.SmallIntegerField(default=90, verbose_name=_('How long (minutes)'))
    is_active = models.BooleanField(default=False, verbose_name=_('Is active'))

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __str__(self):
        return f'{ self.name }'


class Participant(models.Model):
    id = ShortUUIDField(length=8, primary_key=True)
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateField(auto_now=True, verbose_name=_('Updated at'))
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    birth_date = models.DateField(verbose_name=_('Birth date'))
    email = models.EmailField(unique=False, verbose_name=_('Email'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    events = models.ManyToManyField(Event, related_name='event_participants', blank=True, verbose_name=_('Events'))

    class Meta:
        verbose_name = _('Participant')
        verbose_name_plural = _('Participants')

    def __str__(self):
        return f'{ self.name }'