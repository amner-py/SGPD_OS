import json
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.http.response import JsonResponse
from .models import Respuesta,DetalleRespuesta
from ..delegacion.models import Delegacion
from ..formulario.models import *


class ResponderTemplateView(TemplateView):
    template_name='responder.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self,request,id=0):
        try:
            respuestas = Respuesta.objects.last().id+1
        except:
            respuestas=1
        
        print(respuestas)
        if id>0:
            formulario = Formulario.objects.get(id=id)
            preguntas = Pregunta.objects.filter(formulario=id)
            opciones = Opcion.objects.all()
        else:
            preguntas = Pregunta.objects.all()
            opciones = Opcion.objects.all()
        hay_preguntas = len(preguntas)>0
        return render(request,self.template_name,{'preguntas':preguntas,'hay_preguntas':hay_preguntas,'formulario':formulario,'opciones':opciones,'respuestas':respuestas})


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
        return render(request,self.template_name,{'respuestas':respuestas,'hay_respuestas':hay_respuestas,'formulario':id})


class DetalleRespuestaTemplateView(TemplateView):
    template_name='detalles.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0,fr=0):
        if id>0:
            detalles = DetalleRespuesta.objects.filter(respuesta=id)
        else:
            detalles = DetalleRespuesta.objects.all()
        hay_detalles = len(detalles)>0
        return render(request,self.template_name,{'detalles':detalles,'hay_detalles':hay_detalles,'formulario':fr})


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

    def post(self,request):
        jd=json.loads(request.body)
        detalles=jd['respuestas']
        
        respuesta=Respuesta()
        respuesta.latitud=jd['latitud']
        respuesta.longitud=jd['longitud']
        respuesta.delegacion=Delegacion.objects.get(pk=jd['delegacion'])
        respuesta.formulario=Formulario.objects.get(pk=jd['formulario'])
        respuesta.save()

        for detalle in detalles:
            det=DetalleRespuesta()
            det.detalle=detalle['detalle']
            det.pregunta=Pregunta.objects.get(pk=detalle['pregunta'])
            det.respuesta=Respuesta.objects.get(pk=detalle['respuesta'])
            det.save()

        datos={'message':'success'}
        return JsonResponse(datos)


class DetalleRespuestaView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if id>0:
            detalles = list(DetalleRespuesta.objects.filter(respuesta=id).values)
        else:
            detalles=list(DetalleRespuesta.objects.values())

        if len(detalles)>0:
            datos={'message':'success','hay_detalles':True,'detalles':detalles}
        else:
            datos={'message':'wrong','hay_detalles':False}       
        return JsonResponse(datos)


    def post(self,request):
        jd=json.loads(request.body)
        print(jd)
        print(request.method)
        detalle=DetalleRespuesta()
        detalle.detalle=jd['detalle']
        print(f'ULTIMA RESPUESTA{Respuesta.objects.last().id}')
        print(jd['respuesta'])
        #detalle.respuesta=Respuesta.objects.get(pk=jd['respuesta'])
        #detalle.pregunta=Pregunta.objects.get(pk=jd['pregunta'])
        #detalle.save()
        datos={'message':'success'}
        return JsonResponse(datos)