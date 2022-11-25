from django.urls import path
from .views import ReporteTemplateView,ReporteMetaEPTemplateView,ReporteMetaAOTemplateView


urlpatterns = [
    path('reportes/',ReporteTemplateView.as_view(),name='reports_view'),
    path('reportes/meta_eje_prevencion/',ReporteMetaEPTemplateView.as_view(),name='metas_eje_report_view'),
    path('reportes/meta_area_operativa/',ReporteMetaAOTemplateView.as_view(),name='metas_operativa_report_view'),
]