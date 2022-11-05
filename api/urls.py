from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from core.inicio.views import InicioView

urlpatterns = [
    path('panel_control/', admin.site.urls),
    path('',InicioView.as_view(), name='inicio'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('lugar/', include('core.lugar.urls')),
    path('notificacion/', include('core.notificacion.urls')),
    path('asignacion/',include('core.asignacion.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)