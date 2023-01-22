from django.urls import path
from .views import AsignacionView,MetaMensualEPView

urlpatterns = [
    path('api/asignaciones/',AsignacionView.as_view(),name='asignaciones'),
    path('api/metas_eje/',MetaMensualEPView.as_view(),name='metas_eje'),
    path('api/metas_eje/anio/<int:anio>/dele/<int:dele>',MetaMensualEPView.as_view(),name='metas_eje_fil'),
]