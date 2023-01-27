from django.urls import path
from .views import EditarPerfilView

urlpatterns = [
    path('editar/perfil_usuario/',EditarPerfilView.as_view(),name='editar_perfil'),
]