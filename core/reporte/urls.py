from django.urls import path
from .views import ReporteTemplateView,ReporteMetaTemplateView


urlpatterns = [
    path('reportes/',ReporteTemplateView.as_view(),name='reports_view'),
    path('reportes/meta/',ReporteMetaTemplateView.as_view(),name='meta_report_view'),
]