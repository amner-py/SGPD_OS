from django.urls import path
from .views import NotificacionView,NotificacionesListView


urlpatterns = [
    path('notificacion/',NotificacionView.as_view(),name='notificacion'),
    path('notificacion/<int:id>',NotificacionView.as_view(),name='notificacion_process'),
    path('notificaciones/',NotificacionesListView.as_view(),name='notificaciones'),
]