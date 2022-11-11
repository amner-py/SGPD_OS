from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from .models import *

class OperacionView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if id>0:
            operaciones=list(Operacion.objects.filter(operacion=id).values())
            print(operaciones)
            if len(operaciones)>0:
                datos={'message':'success','hay_operacion':True,'operaciones':operaciones}
            else:
                datos={'message':'wrong','hay_operacion':False}
        else:
            operaciones=list(Operacion.objects.values())
            print(operaciones)
            if len(operaciones)>0:
                datos={'message':'success','hay_operacion':True,'operaciones':operaciones}
            else:
                datos={'message':'wrong','hay_operacion':False}
        return JsonResponse(datos)