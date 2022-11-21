from django.urls import path
from .views import OpcionView,FormularioView,PreguntaView,ValidacionView,PreguntaAuxiliarView,SeccionFormularioView,FormularioTemplateView


urlpatterns = [
    path('formularios/<int:id>',FormularioTemplateView.as_view(),name='formularios_list'),
    path('api/opciones/',OpcionView.as_view(),name='opciones_formulario'),
    path('api/formularios/<int:id>',FormularioView.as_view(),name='formularios_id'),
    path('api/formularios/',FormularioView.as_view(),name='formularios'),
    path('api/preguntas/',PreguntaView.as_view(),name='preguntas'),
    path('api/preguntas/<int:id>',PreguntaView.as_view(),name='preguntas_id'),
    path('api/preguntas_auxiliares/',PreguntaAuxiliarView.as_view(),name='preguntas_auxiliares'),
    path('api/validaciones/',ValidacionView.as_view(),name='validaciones'),
    path('api/secciones_formulario/<int:id>',SeccionFormularioView.as_view(),name='secciones_formulario_id'),
    path('api/secciones_formulario/',SeccionFormularioView.as_view(),name='secciones_formulario'),
]