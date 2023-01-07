from django.views.static import serve
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from core.inicio.views import InicioView,page_not_found404
from django.conf.urls import handler404

 
handler404 = page_not_found404

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

    path('panel_control/', admin.site.urls),
    path('',InicioView.as_view(), name='inicio'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('lugar/', include('core.lugar.urls')),
    path('notificacion/', include('core.notificacion.urls')),
    path('asignacion/',include('core.asignacion.urls')),
    path('eje_prevencion/',include('core.eje_prevencion.urls')),
    path('respuesta/',include('core.respuesta.urls')),
    path('reporte/',include('core.reporte.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)