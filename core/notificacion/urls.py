from django.urls import path
from .views import NotificacionView


urlpatterns = [
    path('notificaciones',NotificacionView.as_view(),name='notificacion'),
]