from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

class ReporteTemplateView(TemplateView):
    template_name='reporte.html'
    
    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

class ReporteMetaEPTemplateView(TemplateView):
    template_name='reporte_meta_eje.html'
    
    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

class ReporteMetaAOTemplateView(TemplateView):
    template_name='reporte_meta_operativa.html'
    
    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)