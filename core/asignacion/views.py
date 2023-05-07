from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime as now
from ..delegacion.models import Delegacion
from .models import LugarPriorizado,MetaMensualEP
from ..eje_prevencion.models import EjeTrabajo


class AsignacionView(View):
    
    def get(self,request):
        asignaciones=list(LugarPriorizado.objects.values())
        if len(asignaciones)>0:
            datos={'message':'success','hay_asignacion':True,'asignaciones':asignaciones}
        else:
            datos={'message':'wrong','hay_asignacion':False}
        return JsonResponse(datos)


class MetaMensualEPView(View):
    
    def get(self,request,dele=0,anio=0,eje=0):
        delegaciones={}
        if dele>0 and anio>0 and eje>0:
            metas=MetaMensualEP.objects.filter(asignado__year=f'{anio}',delegacion=dele,eje=eje)
            metas_mes=[0,0,0,0,0,0,0,0,0,0,0,0]
            metas_mes_beneficiarios=[0,0,0,0,0,0,0,0,0,0,0,0]
            metas_alcanzadas=[0,0,0,0,0,0,0,0,0,0,0,0]
            metas_alcanzadas_beneficiarios=[0,0,0,0,0,0,0,0,0,0,0,0]
            delegacion=Delegacion.objects.get(pk=dele)
            eje_trabajo=EjeTrabajo.objects.get(pk=eje)
            for meta in metas:
                metas_mes[meta.asignado.month-1]=meta.meta
                metas_mes_beneficiarios[meta.asignado.month-1]=meta.meta_beneficiarios
                metas_alcanzadas[meta.asignado.month-1]=meta.meta_alcanzada
                metas_alcanzadas_beneficiarios[meta.asignado.month-1]=meta.meta_alcanzada_beneficicarios
            delegaciones={
                'id':dele,
                'delegacion':delegacion.nombre,
                'metas':metas_mes,
                'metas_bene':metas_mes_beneficiarios,
                'alcanzadas':metas_alcanzadas,
                'alcanzadas_bene':metas_alcanzadas_beneficiarios,
                'anio':anio,
                'eje':eje_trabajo.nombre
            }
        return JsonResponse(delegaciones)

class NotificarMeta(View):
    def get(self,request):
        
        metas=MetaMensualEP.objects.filter(delegacion=self.request.user.delegacion)
        fecha=f'{now.now().month}/{now.now().year}'
        mensaje=f'Delegacion: {self.request.user.delegacion}<br>Fecha: {fecha}<br>------------------------------<br>'
        for meta in metas:
            fecha_meta=f'{meta.asignado.month}/{meta.asignado.year}'
            if fecha==fecha_meta:
                mensaje+=f'Eje de Prevención: {meta.eje}<br>Estado Eventos: {meta.eventos()}<br>Estado Beneficiarios: {meta.beneficiarios()}<br>------------------------------<br>'
        data={
            'mensaje':mensaje
        }
        return JsonResponse(data)

class AsignarMetaDelegaciones(TemplateView):
    template_name='asignar_meta_general.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        ejes=EjeTrabajo.objects.all()
        hay_eje=len(ejes)>0
        meta_e=request.GET.get('meta')
        meta_bene=request.GET.get('meta_bene')
        eje_pk=request.GET.get('eje')
        fecha=request.GET.get('asignado')
        
        ingresado=False
        if eje_pk != None:
            asignado=now.strptime(fecha,'%Y-%m-%d')
            eje=EjeTrabajo.objects.get(pk=int(eje_pk))
            delegaciones=Delegacion.objects.all()
            for delegacion in delegaciones:
                meta=MetaMensualEP()
                meta.meta=int(meta_e)
                meta.meta_beneficiarios=int(meta_bene)
                meta.eje=eje
                meta.delegacion=delegacion
                meta.asignado=asignado
                meta.save()
            ingresado=True
        return render(request,self.template_name,{'ejes':ejes,'ingresado':ingresado,'hay_eje':hay_eje})