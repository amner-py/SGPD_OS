from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse
from .models import Notificacion

class NotificacionView(View):
    
    def get(self,request):
        notificaciones=list(Notificacion.objects.values())
        if len(notificaciones)>0:
            datos={'message':'success','hay_notificacion':True,'notificaciones':notificaciones}
        else:
            datos={'message':'wrong','hay_notificacion':False}
        return JsonResponse(datos)