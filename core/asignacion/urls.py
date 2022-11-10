from django.urls import path
from .views import AsignacionView

urlpatterns = [
    path('asignaciones/api/asignaciones',AsignacionView.as_view(),name='asignaciones'),
]