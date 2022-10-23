from django.urls import path
from .views import DepartamentoView


app_name='lugares'


urlpatterns = [
    path('departamento/',DepartamentoView.as_view()),
]