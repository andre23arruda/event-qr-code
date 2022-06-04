from django.db import models
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    time = models.SmallIntegerField()
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __str__(self):
        return f'{ self.name }'


class Participant(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    events = models.ManyToManyField(Event, blank=True)

    class Meta:
        verbose_name = _('Participant')
        verbose_name_plural = _('Participants')

    def __str__(self):
        return f'{ self.name }'