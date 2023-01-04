from django.shortcuts import render
import os
from api import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse
from datetime import datetime
from ..asignacion.models import MetaMensualEP,MetaMensualAO
from ..respuesta.models import EPRespuesta
from django.template.loader import get_template
from weasyprint import HTML,CSS
from weasyprint.text.fonts import FontConfiguration
#from .utils import render_to_pdf

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

class ReporteEjePDF(View):
    template_name='test.html'
    
    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        fecha_inicio=request.GET.get('fecha_inicio')
        fecha_fin=request.GET.get('fecha_fin')
        page=request.GET.get('page',1)
        respuestas=[]

        try:
            es_fecha=datetime.strptime(fecha_inicio,'%Y-%m-%d').date()
        except:
            fecha_inicio=False
        iniciob=False
        finb=False

        if fecha_inicio and fecha_fin:
            print('ambos')
            if self.request.user.is_superuser:
                res= EPRespuesta.objects.filter(respondido__range=[str(fecha_inicio),str(fecha_fin)])
            else:
                res= EPRespuesta.objects.filter(respondido__range=[str(fecha_inicio),str(fecha_fin)]).filter(delegacion=self.request.user)
            iniciob=True
            finb=True
        elif fecha_inicio and not fecha_fin:
            print('inicio')
            if self.request.user.is_superuser:
                res= EPRespuesta.objects.filter(respondido__range=[str(fecha_inicio),str(fecha_inicio)])
            else:
                res= EPRespuesta.objects.filter(respondido__range=[str(fecha_inicio),str(fecha_inicio)]).filter(delegacion=self.request.user)
            iniciob=True
            finb=False
        else:
            print('ninguno')
            if self.request.user.is_superuser:
                res= EPRespuesta.objects.all()
            else:
                res= EPRespuesta.objects.filter(delegacion=self.request.user)
        for re in reversed(res):
            respuestas.append(re)
        hay_respuestas=len(respuestas)>0
        meta=MetaMensualEP.objects.filter(delegacion=self.request.user).last()
        hay_meta=False
        if meta:
            hay_meta=True
        
        data={
            'hay_respuestas':hay_respuestas,
            'entity':respuestas,
            'hay_meta':hay_meta,
            'inicio':fecha_inicio,
            'fin':fecha_fin,
            'iniciob':iniciob,
            'finb':finb,
            'logo':'{}{}'.format(settings.STATIC_URL,'img/logo_pnc.png')
        }
        print('{}{}'.format(settings.STATIC_URL,'img/logo_pnc.png'))
        try:
            template=get_template(self.template_name)
        except:
            pass
        html=template.render(data)
        css_url=os.path.join(settings.BASE_DIR,'static/bootstrap/css/bootstrap.min.css')
        pdf=HTML(string=html,base_url=request.build_absolute_uri()).write_pdf(stylesheets=[CSS(css_url)])
        
        return HttpResponse(pdf,content_type='application/pdf')

#--------------------------------------------------------------------------------------------

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