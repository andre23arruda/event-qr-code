from django.urls import path
from .views import (
    submit_participant_form,
    participant_form,
    success_participant_form,
    error_participant_form,
    see_qrcode,
    see_pdf
)

app_name = 'register_events'

urlpatterns = [
    path('submit_participant/<str:participant_id>', submit_participant_form, name='submit_participant'),
    path('register_participant', participant_form, name='register_participant'),
    path('register_success', success_participant_form, name='register_success'),
    path('register_error', error_participant_form, name='register_error'),
    path('see_qrcode/<str:participant_id>', see_qrcode, name='see_qrcode'),
    path('see_pdf/<str:event_id>/<str:participant_id>', see_pdf, name='see_pdf'),
]