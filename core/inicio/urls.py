from django.urls import path
from .views import PerfilView


urlpatterns = [
    path('delegacion/',PerfilView.as_view(),name='perfil'),
]