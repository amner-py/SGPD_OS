from django.urls import path
from .views import RespuestaTemplateView,RespuestaView


urlpatterns = [
    path('api/respuestas/',RespuestaView.as_view(),name='respuesta'),
    path('respuesta/<int:id>',RespuestaTemplateView.as_view(),name='respuestas'),
]