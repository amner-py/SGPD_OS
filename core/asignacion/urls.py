from django.urls import path
from .views import AsignacionView,MetaMensualEPView,MetaMensualAOView

urlpatterns = [
    path('api/asignaciones/',AsignacionView.as_view(),name='asignaciones'),
    path('api/metas_eje/',MetaMensualEPView.as_view(),name='metas_eje'),
    path('api/metas_eje/anio/<int:anio>/dele/<int:dele>',MetaMensualEPView.as_view(),name='metas_eje_fil'),
    path('api/metas_operativa/anio/<int:anio>/dele/<int:dele>',MetaMensualAOView.as_view(),name='metas_operativa_fil'),
    path('api/metas_operativa/',MetaMensualAOView.as_view(),name='metas_operativa'),
]