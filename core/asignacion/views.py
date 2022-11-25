from django.shortcuts import render
from ..delegacion.models import Delegacion
from .models import Asignacion,MetaMensualEP,MetaMensualAO
from django.http.response import JsonResponse
from django.views import View


class AsignacionView(View):
    
    def get(self,request):
        asignaciones=list(Asignacion.objects.values())
        if len(asignaciones)>0:
            datos={'message':'success','hay_asignacion':True,'asignaciones':asignaciones}
        else:
            datos={'message':'wrong','hay_asignacion':False}
        return JsonResponse(datos)


class MetaMensualEPView(View):
    
    def get(self,request):
        des=Delegacion.objects.all()
        delegaciones=[]
        for delegacion in des:
            ms=MetaMensualEP.objects.filter(delegacion=delegacion.pk)
            metas=[]
            for m in ms:
                metas.append({
                    'meta':m.meta,
                    'alcanzado':m.meta_alcanzada,
                    'mes':m.asignado.month,
                    'anio':m.asignado.year
                })
            delegaciones.append({
                'id':delegacion.pk,
                'nombre':delegacion.delegacion,
                'metas':metas,
            })
            print(delegaciones)
        datos={'message':'success','hay_metas':True,'delegaciones':delegaciones}
        
        return JsonResponse(datos)

class MetaMensualAOView(View):
    
    def get(self,request):
        des=Delegacion.objects.all()
        delegaciones=[]
        for delegacion in des:
            ms=MetaMensualAO.objects.filter(delegacion=delegacion.pk)
            metas=[]
            for m in ms:
                metas.append({
                    'meta':m.meta,
                    'alcanzado':m.meta_alcanzada,
                    'mes':m.asignado.month,
                    'anio':m.asignado.year
                })
            delegaciones.append({
                'id':delegacion.pk,
                'nombre':delegacion.delegacion,
                'metas':metas,
            })
            print(delegaciones)
        datos={'message':'success','hay_metas':True,'delegaciones':delegaciones}
        
        return JsonResponse(datos)