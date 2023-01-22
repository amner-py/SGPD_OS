from django.shortcuts import render
import os
from api import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse
from datetime import datetime
from ..asignacion.models import MetaMensualEP
from ..respuesta.models import EPRespuesta,AORespuesta
from django.template.loader import get_template
from weasyprint import HTML,CSS
from weasyprint.text.fonts import FontConfiguration

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
            if meta.delegacion.nombre not in delegacion_name:
                delegacion_name.append(meta.delegacion.nombre)
                delegaciones.append({
                    'id':meta.delegacion.pk,
                    'nombre':meta.delegacion.nombre
                })
            if meta.asignado.year not in anios:
                anios.append(meta.asignado.year)
        return render(request,self.template_name,{'delegaciones':delegaciones,'anios':anios})

class ReporteEjePDF(View):
    template_name='reporte_eje_prevencion.html'
    
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
            if self.request.user.is_superuser:
                res= EPRespuesta.objects.filter(respondido__range=[str(fecha_inicio),str(fecha_fin)])
            else:
                res= EPRespuesta.objects.filter(respondido__range=[str(fecha_inicio),str(fecha_fin)]).filter(usuario=self.request.user)
            iniciob=True
            finb=True
        elif fecha_inicio and not fecha_fin:
            if self.request.user.is_superuser:
                res= EPRespuesta.objects.filter(respondido__range=[str(fecha_inicio),str(fecha_inicio)])
            else:
                res= EPRespuesta.objects.filter(respondido__range=[str(fecha_inicio),str(fecha_inicio)]).filter(usuario=self.request.user)
            iniciob=True
            finb=False
        else:
            if self.request.user.is_superuser:
                res= EPRespuesta.objects.all()
            else:
                res= EPRespuesta.objects.filter(usuario=self.request.user)
        for re in reversed(res):
            respuestas.append(re)
        hay_respuestas=len(respuestas)>0
        meta=MetaMensualEP.objects.filter(delegacion=self.request.user.delegacion).last()
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

class ReporteGraficaEjePDF(TemplateView):
    template_name='grafica_eje.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        fecha_inicio=request.GET.get('fecha_inicio')
        fecha_fin=request.GET.get('fecha_fin')

        try:
            es_fecha=datetime.strptime(fecha_inicio,'%Y-%m-%d').date()
        except:
            fecha_inicio=False
        if fecha_inicio and fecha_fin:
            if self.request.user.is_superuser:
                respuestas= EPRespuesta.objects.filter(respondido__range=[str(fecha_inicio),str(fecha_fin)])
            else:
                respuestas= EPRespuesta.objects.filter(respondido__range=[str(fecha_inicio),str(fecha_fin)]).filter(usuario=self.request.user)

        elif fecha_inicio and not fecha_fin:
            if self.request.user.is_superuser:
                respuestas= EPRespuesta.objects.filter(respondido__range=[str(fecha_inicio),str(fecha_inicio)])
            else:
                respuestas= EPRespuesta.objects.filter(respondido__range=[str(fecha_inicio),str(fecha_inicio)]).filter(usuario=self.request.user)

        else:
            if self.request.user.is_superuser:
                respuestas= EPRespuesta.objects.all()
            else:
                respuestas= EPRespuesta.objects.filter(usuario=self.request.user)
   
        cantidad_personas=0
        ninios=0
        ninias=0
        adolecentes_masculinos=0
        adolecentes_femeninos=0
        jovenes_masculinos=0
        jovenes_femeninos=0
        adultos_masculinos=0
        adultos_femeninos=0
        adultos_mayores_masculinos=0
        adultos_mayores_femeninos=0
        xincas=0
        garifunas=0
        mayas=0
        ladinos=0
        for respuesta in respuestas:
            cantidad_personas+=respuesta.cantidad_personas
            ninios+=respuesta.ninios
            ninias+=respuesta.ninias
            jovenes_masculinos+=respuesta.jovenes_masculinos
            jovenes_femeninos+=respuesta.jovenes_femeninos
            adolecentes_masculinos+=respuesta.adolecentes_masculinos
            adolecentes_femeninos+=respuesta.adolecentes_femeninos
            adultos_masculinos+=respuesta.adultos_masculinos
            adultos_femeninos+=respuesta.adultos_femeninos
            adultos_mayores_masculinos+=respuesta.adultos_mayores_masculinos
            adultos_mayores_femeninos+=respuesta.adultos_mayores_femeninos
            xincas+=respuesta.xinca
            garifunas+=respuesta.garifuna
            mayas+=respuesta.maya
            ladinos+=respuesta.ladino
        size_respuestas=len(respuestas)

        return render(request,self.template_name,{
            'cantidad_personas':cantidad_personas,
            'ninios':ninios,
            'ninias':ninias,
            'adolecentes_masculinos':adolecentes_masculinos,
            'adolecentes_femeninos':adolecentes_femeninos,
            'jovenes_masculinos':jovenes_masculinos,
            'jovenes_femeninos':jovenes_femeninos,
            'adultos_masculinos':adultos_masculinos,
            'adultos_femeninos':adultos_femeninos,
            'adultos_mayores_masculinos':adultos_mayores_masculinos,
            'adultos_mayores_femeninos':adultos_mayores_femeninos,
            'xincas':xincas,
            'garifunas':garifunas,
            'mayas':mayas,
            'ladinos':ladinos,
            'size_respuestas':size_respuestas
        })

#--------------------------------------------------------------------------------------------

class ReporteAreaPDF(View):
    template_name='reporte_area_operativa.html'
    
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
            if self.request.user.is_superuser:
                res= AORespuesta.objects.filter(respondido__range=[str(fecha_inicio),str(fecha_fin)])
            else:
                res= AORespuesta.objects.filter(respondido__range=[str(fecha_inicio),str(fecha_fin)]).filter(usuario=self.request.user)
            iniciob=True
            finb=True
        elif fecha_inicio and not fecha_fin:
            if self.request.user.is_superuser:
                res= AORespuesta.objects.filter(respondido__range=[str(fecha_inicio),str(fecha_inicio)])
            else:
                res= AORespuesta.objects.filter(respondido__range=[str(fecha_inicio),str(fecha_inicio)]).filter(usuario=self.request.user)
            iniciob=True
            finb=False
        else:
            if self.request.user.is_superuser:
                res= AORespuesta.objects.all()
            else:
                res= AORespuesta.objects.filter(usuario=self.request.user)
        for re in reversed(res):
            respuestas.append(re)
        hay_respuestas=len(respuestas)>0
        
        data={
            'hay_respuestas':hay_respuestas,
            'entity':respuestas,
            'inicio':fecha_inicio,
            'fin':fecha_fin,
            'iniciob':iniciob,
            'finb':finb,
            'logo':'{}{}'.format(settings.STATIC_URL,'img/logo_pnc.png')
        }
        try:
            template=get_template(self.template_name)
        except:
            pass
        html=template.render(data)
        css_url=os.path.join(settings.BASE_DIR,'static/bootstrap/css/bootstrap.min.css')
        pdf=HTML(string=html,base_url=request.build_absolute_uri()).write_pdf(stylesheets=[CSS(css_url)])
        
        return HttpResponse(pdf,content_type='application/pdf')


class ReporteGraficaAreaPDF(TemplateView):
    template_name='grafica_area.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        fecha_inicio=request.GET.get('fecha_inicio')
        fecha_fin=request.GET.get('fecha_fin')

        try:
            es_fecha=datetime.strptime(fecha_inicio,'%Y-%m-%d').date()
        except:
            fecha_inicio=False
        if fecha_inicio and fecha_fin:
            if self.request.user.is_superuser:
                respuestas= AORespuesta.objects.filter(respondido__range=[str(fecha_inicio),str(fecha_fin)])
            else:
                respuestas= AORespuesta.objects.filter(respondido__range=[str(fecha_inicio),str(fecha_fin)]).filter(usuario=self.request.user)

        elif fecha_inicio and not fecha_fin:
            if self.request.user.is_superuser:
                respuestas= AORespuesta.objects.filter(respondido__range=[str(fecha_inicio),str(fecha_inicio)])
            else:
                respuestas= AORespuesta.objects.filter(respondido__range=[str(fecha_inicio),str(fecha_inicio)]).filter(usuario=self.request.user)

        else:
            if self.request.user.is_superuser:
                respuestas= AORespuesta.objects.all()
            else:
                respuestas= AORespuesta.objects.filter(usuario=self.request.user)
   
        total_identificados=0
        hombres_identificados=0
        mujeres_identificadas=0
        autos_identificados=0
        motos_identificadas=0
        armas_identificadas=0
        total_consignados=0
        hombres_consignados=0
        mujeres_consignadas=0
        autos_consignados=0
        motos_consignadas=0
        armas_consignadas=0
        total_conducidos=0
        hombres_conducidos=0
        mujeres_conducidas=0
        total_solventes=0
        hombres_solventes=0
        mujeres_solventes=0
        autos_solventes=0
        motos_solventes=0
        armas_solventes=0
        total_recuperados=0
        autos_recuperados=0
        motos_recuperados=0
        armas_recuperados=0
        hombres_recuperados=0
        mujeres_recuperadas=0
        menores_recuperados=0
        for respuesta in respuestas:
            total_identificados+=respuesta.total_identificados
            hombres_identificados+=respuesta.hombres_identificados
            mujeres_identificadas+=respuesta.mujeres_identificadas
            autos_identificados+=respuesta.autos_identificados
            motos_identificadas+=respuesta.motos_identificadas
            armas_identificadas+=respuesta.armas_identificadas
            total_consignados+=respuesta.total_consignados
            hombres_consignados+=respuesta.hombres_consignados
            mujeres_consignadas+=respuesta.mujeres_consignadas
            autos_consignados+=respuesta.autos_consignados
            motos_consignadas+=respuesta.motos_consignadas
            armas_consignadas+=respuesta.armas_consignadas
            total_conducidos+=respuesta.total_conducidos
            hombres_conducidos+=respuesta.hombres_conducidos
            mujeres_conducidas+=respuesta.mujeres_conducidas
            total_solventes+=respuesta.total_solventes
            hombres_solventes+=respuesta.hombres_solventes
            mujeres_solventes+=respuesta.mujeres_solventes
            autos_solventes+=respuesta.autos_solventes
            motos_solventes+=respuesta.motos_solventes
            armas_solventes+=respuesta.armas_solventes
            total_recuperados+=respuesta.total_recuperados
            autos_recuperados+=respuesta.autos_recuperados
            motos_recuperados+=respuesta.motos_recuperados
            armas_recuperados+=respuesta.armas_recuperados
            hombres_recuperados+=respuesta.hombres_recuperados
            mujeres_recuperadas+=respuesta.mujeres_recuperadas
            menores_recuperados+=respuesta.menores_recuperados
        size_respuestas=len(respuestas)

        return render(request,self.template_name,{
            'total_identificados':total_identificados,
            'hombres_identificados':hombres_identificados,
            'mujeres_identificadas':mujeres_identificadas,
            'autos_identificados':autos_identificados,
            'motos_identificadas':motos_identificadas,
            'armas_identificadas':armas_identificadas,
            'total_consignados':total_consignados,
            'hombres_consignados':hombres_consignados,
            'mujeres_consignadas':mujeres_consignadas,
            'autos_consignados':autos_consignados,
            'motos_consignadas':motos_consignadas,
            'armas_consignadas':armas_consignadas,
            'total_conducidos':total_conducidos,
            'hombres_conducidos':hombres_conducidos,
            'mujeres_conducidas':mujeres_conducidas,
            'total_solventes':total_solventes,
            'hombres_solventes':hombres_solventes,
            'mujeres_solventes':mujeres_solventes,
            'autos_solventes':autos_solventes,
            'motos_solventes':motos_solventes,
            'armas_solventes':armas_solventes,
            'total_recuperados':total_recuperados,
            'autos_recuperados':autos_recuperados,
            'motos_recuperados':motos_recuperados,
            'armas_recuperados':armas_recuperados,
            'hombres_recuperados':hombres_recuperados,
            'mujeres_recuperadas':mujeres_recuperadas,
            'menores_recuperados':menores_recuperados,
            'size_respuestas':size_respuestas
        })