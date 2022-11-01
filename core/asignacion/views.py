from django.shortcuts import render
from .models import Asignacion
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
    
    
    def post(self,request):
        pass


    def put(self,request):
        pass


    def delete(self,request):
        pass