from django.urls import path
from .views import AsignacionView,MetaMensualEPView,AsignarMetaDelegaciones,NotificarMeta

urlpatterns = [
    path('api/asignaciones/',AsignacionView.as_view(),name='asignaciones'),
    path('api/metas_eje/',MetaMensualEPView.as_view(),name='metas_eje'),
    path('asignar/metas_eje/',AsignarMetaDelegaciones.as_view(),name='asignar_metas_eje'),
    path('api/metas_eje/anio/<int:anio>/dele/<int:dele>/eje/<int:eje>',MetaMensualEPView.as_view(),name='metas_eje_fil'),
    path('notificar/metas_eje/',NotificarMeta.as_view(),name='notificar_metas_eje'),
]