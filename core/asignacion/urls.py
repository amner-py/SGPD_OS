from django.urls import path
from .views import AsignacionView,MetaMensualEPView,MetaMensualAOView

urlpatterns = [
    path('api/asignaciones/',AsignacionView.as_view(),name='asignaciones'),
    path('api/metas_eje/',MetaMensualEPView.as_view(),name='metas_eje'),
    path('api/metas_operativa/',MetaMensualAOView.as_view(),name='metas_operativa'),
]