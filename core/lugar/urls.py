from django.urls import path
from .views import DepartamentoView,DepaChiquimulaView,ChiquiSanJoseLaAradaView,EsquipulasView


urlpatterns = [
    path('departamento/',DepartamentoView.as_view(),name='departamentos'),
    path('chiquimula/',DepaChiquimulaView.as_view(),name='depa_chiquimula'),
    path('chiquimula/sanjoselaarada',ChiquiSanJoseLaAradaView.as_view(),name='san_jose_la_arada'),
    path('chiquimula/esquipulas',EsquipulasView.as_view(),name='esquipulas'),
]