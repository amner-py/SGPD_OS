from django.urls import path
from .views import RespuestaTemplateView,RespuestaView,ResponderTemplateView,DetalleRespuestaView,DetalleRespuestaTemplateView


urlpatterns = [
    path('api/respuestas/',RespuestaView.as_view(),name='respuesta'),
    path('api/detalles/',DetalleRespuestaView.as_view(),name='detalle'),
    path('respuesta/<int:id>',RespuestaTemplateView.as_view(),name='respuestas'),
    path('respuesta/<int:fr>/detalles/<int:id>',DetalleRespuestaTemplateView.as_view(),name='detalles_view'),
    path('responder/<int:id>',ResponderTemplateView.as_view(),name='responder'),
]