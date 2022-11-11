from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.http.response import JsonResponse
from .models import *


class FormularioTemplateView(TemplateView):
    template_name='formularios.html'
    
    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self,request,id,*args,**kwargs):
        formularios=Formulario.objects.filter(operacion=id)
        hay_formulario=len(formularios)>0
        return render(request,self.template_name,{'formularios':formularios,'hay_formulario':hay_formulario})


class FormularioView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if id>0:
            formularios=list(Formulario.objects.filter(operacion=id).values())
            print(formularios)
            if len(formularios)>0:
                datos={'message':'success','hay_formulario':True,'formularios':formularios}
            else:
                datos={'message':'wrong','hay_formulario':False}
        else:
            formularios=list(Formulario.objects.values())
            print(formularios)
            if len(formularios)>0:
                datos={'message':'success','hay_formulario':True,'formularios':formularios}
            else:
                datos={'message':'wrong','hay_formulario':False}
        return JsonResponse(datos)


class SeccionFormularioView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if id>0:
            seccion_formulario=list(SeccionFormulario.objects.filter(formulario=id).values())
            if len(seccion_formulario)>0:
                datos={'message':'success','hay_seccion_formulario':True,'seccion_formulario':seccion_formulario}
            else:
                datos={'message':'wrong','hay_seccion_formulario':False}
        else:
            seccion_formulario=list(SeccionFormulario.objects.values())
            if len(seccion_formulario)>0:
                datos={'message':'success','hay_seccion_formulario':True,'seccion_formulario':seccion_formulario}
            else:
                datos={'message':'wrong','hay_seccion_formulario':False}
        return JsonResponse(datos)


class PreguntaView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if id>0:
            preguntas=list(Pregunta.objects.filter(formulario=id).values())
            if len(preguntas)>0:
                datos={'message':'success','hay_pregunta':True,'preguntas':preguntas}
            else:
                datos={'message':'wrong','hay_pregunta':False}
        else:
            preguntas=list(Pregunta.objects.values())
            if len(preguntas)>0:
                datos={'message':'success','hay_pregunta':True,'preguntas':preguntas}
            else:
                datos={'message':'wrong','hay_pregunta':False}        
        return JsonResponse(datos)


class PreguntaAuxiliarView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        preguntas_auxiliares=list(PreguntaAuxiliar.objects.values())
        if len(preguntas_auxiliares)>0:
            datos={'message':'success','hay_pregunta_auxiliar':True,'preguntas_auxiliares':preguntas_auxiliares}
        else:
            datos={'message':'wrong','hay_pregunta_auxiliar':False}
        return JsonResponse(datos)

class ValidacionView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        validaciones=list(Validacion.objects.values())
        if len(validaciones)>0:
            datos={'message':'success','hay_validacion':True,'validaciones':validaciones}
        else:
            datos={'message':'wrong','hay_validacion':False}
        return JsonResponse(datos)


class OpcionView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        opciones=list(Opcion.objects.values())
        if len(opciones)>0:
            datos={'message':'success','hay_opcion':True,'opciones':opciones}
        else:
            datos={'message':'wrong','hay_opcion':False}
        return JsonResponse(datos)