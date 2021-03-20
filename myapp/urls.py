from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import static
from . import settings

urlpatterns = [
    path('lunchmap/', include('lunchmap.urls')),
    path('admin/', admin.site.urls),
    path('',  RedirectView.as_view(url='/lunchmap/')),
]
urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)