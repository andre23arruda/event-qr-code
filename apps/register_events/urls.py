from django.urls import path
from .views import *

urlpatterns = [
    path('register_participant', participant_form, name='register_participant'),
    path('submit_participant/<int:participant_id>', submit_partipant_form, name='submit_participant'),
    path('register_success', view_register_success, name='register_success'),
    path('register_error', view_register_error, name='register_error'),
]