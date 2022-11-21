from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from core.inicio.views import InicioView
from core.inicio.views import get_error_404
from django.conf.urls import handler404

 
handler404 = get_error_404

urlpatterns = [
    path('panel_control/', admin.site.urls),
    path('',InicioView.as_view(), name='inicio'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('lugar/', include('core.lugar.urls')),
    path('notificacion/', include('core.notificacion.urls')),
    path('respuesta/', include('core.respuesta.urls')),
    path('asignacion/',include('core.asignacion.urls')),
    path('formulario/',include('core.formulario.urls')),
    path('operacion/',include('core.operacion.urls')),
    path('reporte/',include('core.reporte.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)