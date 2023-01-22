from django.urls import path
from .views import ReporteTemplateView,ReporteMetaEPTemplateView,ReporteEjePDF,ReporteAreaPDF,ReporteGraficaEjePDF,ReporteGraficaAreaPDF


urlpatterns = [
    path('reportes/',ReporteTemplateView.as_view(),name='reports_view'),
    path('reportes/eje_prevencion/pdf/',ReporteEjePDF.as_view(),name='reporte_eje_view'),
    path('reportes/area_operativa/pdf/',ReporteAreaPDF.as_view(),name='reporte_area_view'),
    path('reportes/graficas/eje_prevencion/',ReporteGraficaEjePDF.as_view(),name='reporte_grafica_eje_view'),
    path('reportes/graficas/area_operativa/',ReporteGraficaAreaPDF.as_view(),name='reporte_grafica_area_view'),
    path('reportes/meta_eje_prevencion/',ReporteMetaEPTemplateView.as_view(),name='metas_eje_report_view'),
]