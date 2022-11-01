from django.urls import path
from .views import AsignacionView

urlpatterns = [
    path('asignaciones',AsignacionView.as_view(),name='asignaciones'),
]