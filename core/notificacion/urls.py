from django.urls import path
from .views import NotificacionView,NotificacionesTemplateView


urlpatterns = [
    path('api/notificaciones/',NotificacionView.as_view(),name='notificacion'),
    path('actualizacion/<int:id>',NotificacionView.as_view(),name='notificacion_process'),
    path('notificaciones/',NotificacionesTemplateView.as_view(),name='notificaciones'),
]