from django.urls import path
from .views import *

urlpatterns = [
    path('register_participant', view_render_partipant, name='register_participant'),
    path('submit_participant/<int:participant_id>', view_submit_partipant, name='submit_participant'),
    path('register_success', view_register_success, name='register_success'),
    path('register_error', view_register_error, name='register_error'),
]