from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from ..asignacion.models import MetaMensualEP,MetaMensualAO

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

    def get(self,request):
        metas=MetaMensualEP.objects.all()
        delegaciones=[]
        delegacion_name=[]
        anios=[]
        for meta in metas:
            if meta.delegacion.delegacion not in delegacion_name:
                delegacion_name.append(meta.delegacion.delegacion)
                delegaciones.append({
                    'id':meta.delegacion.pk,
                    'nombre':meta.delegacion.delegacion
                })
            if meta.asignado.year not in anios:
                anios.append(meta.asignado.year)
        return render(request,self.template_name,{'delegaciones':delegaciones,'anios':anios})


class ReporteMetaAOTemplateView(TemplateView):
    template_name='reporte_meta_operativa.html'
    
    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        metas=MetaMensualAO.objects.all()
        delegaciones=[]
        delegacion_name=[]
        anios=[]
        for meta in metas:
            if meta.delegacion.delegacion not in delegacion_name:
                delegacion_name.append(meta.delegacion.delegacion)
                delegaciones.append({
                    'id':meta.delegacion.pk,
                    'nombre':meta.delegacion.delegacion
                })
            if meta.asignado.year not in anios:
                anios.append(meta.asignado.year)
        return render(request,self.template_name,{'delegaciones':delegaciones,'anios':anios})