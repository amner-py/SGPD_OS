from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.http.response import JsonResponse
from .models import Respuesta

class RespuestaTemplateView(TemplateView):
    template_name='respuesta.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if id>0:
            respuestas = Respuesta.objects.filter(formulario=id)
        else:
            respuestas = Respuesta.objects.all()
        hay_respuestas = len(respuestas)>0
        return render(request,self.template_name,{'respuestas':respuestas,'hay_respuestas':hay_respuestas})


class RespuestaView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        respuestas=list(Respuesta.objects.values())
        if len(respuestas)>0:
            datos={'message':'success','hay_respuesta':True,'respuestas':respuestas}
        else:
            datos={'message':'wrong','hay_respuesta':False}
        return JsonResponse(datos)