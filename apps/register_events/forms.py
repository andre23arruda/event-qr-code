import datetime
from django import forms
from .models import Event, Participant
from .utils import available_events

today = datetime.datetime.now()
today = today.replace(hour=0, minute=0, second=0, microsecond=0)
tomorrow = today + datetime.timedelta(1)

class ParticipantForms(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ParticipantForms, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    event = forms.ModelChoiceField(queryset=Event.objects.all())
    # event = forms.ModelChoiceField(queryset=Event.objects.filter(date__gte=datetime.now()))
    # event = forms.ModelChoiceField(queryset=available_events())

    class Meta:
        model = Participant
        fields = ['name', 'description', 'event']

        widgets = {
            'name': forms.TextInput(attrs={
                'disabled': '',
            }),
            'description': forms.Textarea(attrs={
                'disabled': '',
                'rows': '5',
            }),
        }


    def clean(self):
        return self.cleaned_data
