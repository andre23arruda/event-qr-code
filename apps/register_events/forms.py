import datetime
from django import forms
from .models import Event, Participant
from .utils import available_events

today = datetime.datetime.now()
today = today.replace(hour=0, minute=0, second=0, microsecond=0)
tomorrow = today + datetime.timedelta(1)

class ParticipantForms(forms.ModelForm):
    event = forms.ModelChoiceField(
        queryset=Event.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    # event = forms.ModelChoiceField(
    #     queryset=Event.objects.filter(date__gte=datetime.now()),
    #     widget=forms.Select(attrs={'class': 'form-control'})
    # )
    # event = forms.ModelChoiceField(
    #     queryset=available_events(),
    #     widget=forms.Select(attrs={'class': 'form-control'})
    # )

    class Meta:
        model = Participant
        fields = ['name', 'birth_date', 'email', 'description', 'event']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': '',
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'data-parentclass': 'col-lg-6',
                'disabled': '',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-parentclass': 'col-lg-6',
                'disabled': '',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'disabled': '',
                'rows': '5',
            }),
        }


    def clean(self):
        return self.cleaned_data
