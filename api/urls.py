from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from core.inicio.views import InicioView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',InicioView.as_view(), name='inicio'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('lugar/', include('core.lugar.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)