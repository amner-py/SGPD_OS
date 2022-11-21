from django.urls import path
from .views import AsignacionView,MetaMensualView

urlpatterns = [
    path('api/asignaciones/',AsignacionView.as_view(),name='asignaciones'),
    path('api/metas/',MetaMensualView.as_view(),name='metas_alcanzadas'),
]