from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
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
            metas_alcanzadas=[0,0,0,0,0,0,0,0,0,0,0,0]
            delegacion=Delegacion.objects.get(pk=dele)
            eje_trabajo=EjeTrabajo.objects.get(pk=eje)
            for meta in metas:
                metas_mes[meta.asignado.month-1]=meta.meta
                metas_alcanzadas[meta.asignado.month-1]=meta.meta_alcanzada
            delegaciones={
                'id':dele,
                'delegacion':delegacion.nombre,
                'metas':metas_mes,
                'alcanzadas':metas_alcanzadas,
                'anio':anio,
                'eje':eje_trabajo.nombre
            }
        return JsonResponse(delegaciones)
