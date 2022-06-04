from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static # media

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register_events/', include('register_events.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # media
