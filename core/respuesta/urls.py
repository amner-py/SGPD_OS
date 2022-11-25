from django.urls import path
from .views import *


urlpatterns = [
    path('respuestas/eje_prevencion/',RespuestasEPTemplateView.as_view(),name='respuestas_eje_view'),
    path('respuestas/eje_prevencion/responder',ResponderEPTemplateView.as_view(),name='responder_eje'),
    path('respuestas/eje_prevencion/actualizar/<int:id>',ActualizarEPTemplateView.as_view(),name='actualizar_eje'),
    path('api/respuestas/eje_prevencion/',RespuestasEPView.as_view(),name='respuesta_eje_api'),
    path('respuesta/eje_prevencion/<int:id>',InformeEPTemplateView.as_view(),name='respuesta_eje_inf'),

    path('respuestas/area_operativa/',RespuestasAOTemplateView.as_view(),name='respuestas_operativo_view'),
    path('respuestas/area_operativa/responder',ResponderAOTemplateView.as_view(),name='responder_operativo'),
    path('api/respuestas/area_operativa/',RespuestasAOView.as_view(),name='respuesta_operativo_api'),
    path('respuesta/area_operativa/<int:id>',InformeAOTemplateView.as_view(),name='respuesta_operativo_inf'),
    path('respuestas/area_operativa/actualizar/<int:id>',ActualizarAOTemplateView.as_view(),name='actualizar_operativo'),
]