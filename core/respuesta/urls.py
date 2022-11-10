from django.urls import path
from .views import RespuestaTemplateView,RespuestaView


urlpatterns = [
    path('api/respuestas/',RespuestaView.as_view(),name='respuesta'),
    path('respuesta/',RespuestaTemplateView.as_view(),name='respuestas'),
]