import json
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.http.response import JsonResponse
from .models import EPRespuesta,AORespuesta
from ..asignacion.models import Asignacion,MetaMensualEP,MetaMensualAO
from ..operacion.models import *


class RespuestasEPTemplateView(TemplateView):
    template_name='respuestas_eje.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        res= EPRespuesta.objects.all()
        respuestas=[]
        for re in reversed(res):
            respuestas.append(re)
        hay_respuestas=len(respuestas)>0
        meta=MetaMensualEP.objects.filter(delegacion=self.request.user).last()
        hay_meta=False
        if meta:
            hay_meta=True
        return render(request,self.template_name,{
            'hay_respuestas':hay_respuestas,
            'respuestas':respuestas,
            'hay_meta':hay_meta
        })

class ActualizarEPTemplateView(TemplateView):
    template_name='update_eje.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,id=0):
        if id>0:
            lugares_asignados=Asignacion.objects.filter(delegacion=self.request.user)
            res=EPRespuesta.objects.get(pk=id)
            planes=Plan.objects.filter(operacion=1)
            ejes=EjeTrabajo.objects.filter(operacion=1)
            productos=Producto.objects.filter(operacion=1)
        return render(request,self.template_name,{
            'res':res,
            'planes':planes,
            'ejes':ejes,
            'productos':productos,
            'lugares_asignados':lugares_asignados
        })

class ResponderEPTemplateView(TemplateView):
    template_name='form_eje.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        lugares_asignados=Asignacion.objects.filter(delegacion=self.request.user)
        meta=MetaMensualEP.objects.filter(delegacion=self.request.user).last()
        hay_meta=False
        if meta:
            hay_meta=True
        planes=Plan.objects.filter(operacion=1)
        ejes=EjeTrabajo.objects.filter(operacion=1)
        productos=Producto.objects.filter(operacion=1)
        hay_datos=len(lugares_asignados)>0 and len(planes)>0 and len(ejes)>0 and len(productos)>0 and hay_meta
        return render(request,self.template_name,{
            'lugares_asignados':lugares_asignados,
            'planes':planes,
            'ejes':ejes,
            'productos':productos,
            'hay_datos':hay_datos
        })

class InformeEPTemplateView(TemplateView):
    template_name='informe_eje.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,id=0):
        if id>0:
            respuesta=EPRespuesta.objects.get(pk=id)
        return render(request,self.template_name,{
            'respuesta':respuesta,
        })


class RespuestasEPView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        respuestas=list(EPRespuesta.objects.values())
        if len(respuestas)>0:
            datos={'message':'success','hay_respuestas':True,'respuestas':respuestas}
        else:
            datos={'message':'wrong','hay_respuestas':False}
        return JsonResponse(datos)

    
    def post(self,request):
        jd=json.loads(request.body)
        respuesta=EPRespuesta()
        respuesta.latitud=jd['latitud']
        respuesta.longitud=jd['longitud']
        respuesta.delegacion=self.request.user
        respuesta.asignado=Asignacion.objects.get(pk=jd['lugar_asignado'])
        respuesta.lugar_especifico=jd['lugar_especifico']
        respuesta.plan=Plan.objects.get(pk=jd['plan'])
        respuesta.eje=EjeTrabajo.objects.get(pk=jd['eje'])
        respuesta.producto=Producto.objects.get(pk=jd['producto'])
        respuesta.subproducto=Subproducto.objects.get(pk=jd['subproducto'])
        respuesta.observaciones=jd['observaciones']
        respuesta.cantidad_personas=jd['cantidad_personas']
        respuesta.ninios=jd['ninios']
        respuesta.ninias=jd['ninias']
        respuesta.adolecentes_masculinos=jd['adolecentes_masculinos']
        respuesta.adolecentes_femeninos=jd['adolecentes_femeninas']
        respuesta.jovenes_masculinos=jd['jovenes_masculinos']
        respuesta.jovenes_femeninos=jd['jovenes_femeninas']
        respuesta.adultos_masculinos=jd['adultos']
        respuesta.adultos_femeninos=jd['adultas']
        respuesta.adultos_mayores_masculinos=jd['adultos_mayores']
        respuesta.adultos_mayores_femeninos=jd['adultas_mayores']
        respuesta.xinca=jd['xincas']
        respuesta.garifuna=jd['garifunas']
        respuesta.maya=jd['mayas']
        respuesta.ladino=jd['ladinos']
        ingresado=respuesta.save()
        datos={'ingresado':ingresado}
        return JsonResponse(datos)

    def put(self,request):
        jd=json.loads(request.body)
        respuesta=EPRespuesta.objects.get(pk=jd['id'])
        respuesta.latitud=jd['latitud']
        respuesta.longitud=jd['longitud']
        respuesta.delegacion=self.request.user
        respuesta.asignado=Asignacion.objects.get(pk=jd['lugar_asignado'])
        respuesta.lugar_especifico=jd['lugar_especifico']
        respuesta.plan=Plan.objects.get(pk=jd['plan'])
        respuesta.eje=EjeTrabajo.objects.get(pk=jd['eje'])
        respuesta.producto=Producto.objects.get(pk=jd['producto'])
        respuesta.subproducto=Subproducto.objects.get(pk=jd['subproducto'])
        respuesta.observaciones=jd['observaciones']
        respuesta.cantidad_personas=jd['cantidad_personas']
        respuesta.ninios=jd['ninios']
        respuesta.ninias=jd['ninias']
        respuesta.adolecentes_masculinos=jd['adolecentes_masculinos']
        respuesta.adolecentes_femeninos=jd['adolecentes_femeninas']
        respuesta.jovenes_masculinos=jd['jovenes_masculinos']
        respuesta.jovenes_femeninos=jd['jovenes_femeninas']
        respuesta.adultos_masculinos=jd['adultos']
        respuesta.adultos_femeninos=jd['adultas']
        respuesta.adultos_mayores_masculinos=jd['adultos_mayores']
        respuesta.adultos_mayores_femeninos=jd['adultas_mayores']
        respuesta.xinca=jd['xincas']
        respuesta.garifuna=jd['garifunas']
        respuesta.maya=jd['mayas']
        respuesta.ladino=jd['ladinos']
        respuesta._ACTUALIZAR=True
        ingresado=respuesta.save()
        datos={'ingresado':ingresado}
        return JsonResponse(datos)

    def delete(self,request):
        jd=json.loads(request.body)
        respuesta=EPRespuesta.objects.get(pk=jd['id'])
        eliminado=respuesta.delete()
        datos={'eliminado':eliminado}
        return JsonResponse(datos)

#-----------------------------------------------------------------------------


class RespuestasAOTemplateView(TemplateView):
    template_name='respuestas_operativo.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        res= AORespuesta.objects.all()
        respuestas=[]
        for re in reversed(res):
            respuestas.append(re)
        hay_respuestas=len(respuestas)>0
        meta=MetaMensualAO.objects.filter(delegacion=self.request.user).last()
        hay_meta=False
        if meta:
            hay_meta=True
        return render(request,self.template_name,{
            'hay_respuestas':hay_respuestas,
            'respuestas':respuestas,
            'hay_meta':hay_meta
        })

class ResponderAOTemplateView(TemplateView):
    template_name='form_operativo.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        lugares_asignados=Asignacion.objects.filter(delegacion=self.request.user)
        meta=MetaMensualAO.objects.filter(delegacion=self.request.user).last()
        hay_meta=False
        if meta:
            hay_meta=True
        planes=Plan.objects.filter(operacion=2)
        operativos=TipoOperativo.objects.filter(operacion=2)
        hay_datos=len(lugares_asignados)>0 and len(planes)>0 and len(operativos)>0 and hay_meta
        return render(request,self.template_name,{
            'lugares_asignados':lugares_asignados,
            'planes':planes,
            'operativos':operativos,
            'hay_datos':hay_datos
        })

class RespuestasAOView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        respuestas=list(AORespuesta.objects.values())
        if len(respuestas)>0:
            datos={'message':'success','hay_respuestas':True,'respuestas':respuestas}
        else:
            datos={'message':'wrong','hay_respuestas':False}
        return JsonResponse(datos)

    def post(self,request):
        jd=json.loads(request.body)
        respuesta=AORespuesta()
        respuesta.latitud=jd['latitud']
        respuesta.longitud=jd['longitud']
        respuesta.delegacion=self.request.user
        respuesta.asignado=Asignacion.objects.get(pk=jd['asignado'])
        respuesta.lugar_apoyo=jd['lugar_apoyo']
        respuesta.plan=Plan.objects.get(pk=jd['plan'])
        respuesta.operativo=TipoOperativo.objects.get(pk=jd['operativo'])
        respuesta.observaciones=jd['observaciones']
        respuesta.total_identificados=jd['total_identificados']
        respuesta.hombres_identificados=jd['hombres_identificados']
        respuesta.mujeres_identificadas=jd['mujeres_identificadas']
        respuesta.autos_identificados=jd['autos_identificados']
        respuesta.motos_identificadas=jd['motos_identificadas']
        respuesta.armas_identificadas=jd['armas_identificadas']
        respuesta.total_consignados=jd['total_consignados']
        respuesta.hombres_consignados=jd['hombres_consignados']
        respuesta.mujeres_consignadas=jd['mujeres_consignadas']
        respuesta.autos_consignados=jd['autos_consignados']
        respuesta.motos_consignadas=jd['motos_consignadas']
        respuesta.armas_consignadas=jd['armas_consignadas']
        respuesta.total_conducidos=jd['total_conducidos']
        respuesta.hombres_conducidos=jd['hombres_conducidos']
        respuesta.mujeres_conducidas=jd['mujeres_conducidas']
        respuesta.total_solventes=jd['total_solventes']
        respuesta.hombres_solventes=jd['hombres_solventes']
        respuesta.mujeres_solventes=jd['mujeres_solventes']
        respuesta.autos_solventes=jd['autos_solventes']
        respuesta.motos_solventes=jd['motos_solventes']
        respuesta.armas_solventes=jd['armas_solventes']
        respuesta.total_recuperados=jd['total_recuperados']
        respuesta.autos_recuperados=jd['autos_recuperados']
        respuesta.motos_recuperados=jd['motos_recuperados']
        respuesta.armas_recuperados=jd['armas_recuperados']
        respuesta.hombres_recuperados=jd['hombres_recuperados']
        respuesta.mujeres_recuperadas=jd['mujeres_recuperadas']
        respuesta.menores_recuperados=jd['menores_recuperados']
        ingresado=respuesta.save()
        datos={'ingresado':ingresado}
        return JsonResponse(datos)

    def put(self,request):
        jd=json.loads(request.body)
        respuesta=AORespuesta.objects.get(pk=jd['id'])
        respuesta.latitud=jd['latitud']
        respuesta.longitud=jd['longitud']
        respuesta.delegacion=self.request.user
        respuesta.asignado=Asignacion.objects.get(pk=jd['asignado'])
        respuesta.lugar_apoyo=jd['lugar_apoyo']
        respuesta.plan=Plan.objects.get(pk=jd['plan'])
        respuesta.operativo=TipoOperativo.objects.get(pk=jd['operativo'])
        respuesta.observaciones=jd['observaciones']
        respuesta.total_identificados=jd['total_identificados']
        respuesta.hombres_identificados=jd['hombres_identificados']
        respuesta.mujeres_identificadas=jd['mujeres_identificadas']
        respuesta.autos_identificados=jd['autos_identificados']
        respuesta.motos_identificadas=jd['motos_identificadas']
        respuesta.armas_identificadas=jd['armas_identificadas']
        respuesta.total_consignados=jd['total_consignados']
        respuesta.hombres_consignados=jd['hombres_consignados']
        respuesta.mujeres_consignadas=jd['mujeres_consignadas']
        respuesta.autos_consignados=jd['autos_consignados']
        respuesta.motos_consignadas=jd['motos_consignadas']
        respuesta.armas_consignadas=jd['armas_consignadas']
        respuesta.total_conducidos=jd['total_conducidos']
        respuesta.hombres_conducidos=jd['hombres_conducidos']
        respuesta.mujeres_conducidas=jd['mujeres_conducidas']
        respuesta.total_solventes=jd['total_solventes']
        respuesta.hombres_solventes=jd['hombres_solventes']
        respuesta.mujeres_solventes=jd['mujeres_solventes']
        respuesta.autos_solventes=jd['autos_solventes']
        respuesta.motos_solventes=jd['motos_solventes']
        respuesta.armas_solventes=jd['armas_solventes']
        respuesta.total_recuperados=jd['total_recuperados']
        respuesta.autos_recuperados=jd['autos_recuperados']
        respuesta.motos_recuperados=jd['motos_recuperados']
        respuesta.armas_recuperados=jd['armas_recuperados']
        respuesta.hombres_recuperados=jd['hombres_recuperados']
        respuesta.mujeres_recuperadas=jd['mujeres_recuperadas']
        respuesta.menores_recuperados=jd['menores_recuperados']
        respuesta._ACTUALIZAR=True
        ingresado=respuesta.save()
        datos={'ingresado':ingresado}
        return JsonResponse(datos)

    def delete(self,request):
            jd=json.loads(request.body)
            respuesta=AORespuesta.objects.get(pk=jd['id'])
            eliminado=respuesta.delete()
            datos={'eliminado':eliminado}
            return JsonResponse(datos)

class InformeAOTemplateView(TemplateView):
    template_name='informe_operativo.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,id=0):
        if id>0:
            respuesta=AORespuesta.objects.get(pk=id)
        return render(request,self.template_name,{
            'respuesta':respuesta,
        })

class ActualizarAOTemplateView(TemplateView):
    template_name='update_operativo.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,id=0):
        if id>0:
            lugares_asignados=Asignacion.objects.filter(delegacion=self.request.user)
            res=AORespuesta.objects.get(pk=id)
            planes=Plan.objects.filter(operacion=2)
            operativos=TipoOperativo.objects.filter(operacion=2)
        return render(request,self.template_name,{
            'res':res,
            'planes':planes,
            'operativos':operativos,
            'lugares_asignados':lugares_asignados
        })