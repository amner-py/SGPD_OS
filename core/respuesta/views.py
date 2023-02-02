import json
from django.views import View
from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView,ListView
from django.http.response import JsonResponse
from django.core.paginator import Paginator
from django.http import Http404
from datetime import datetime as now
from .models import EPRespuesta,AORespuesta
from ..asignacion.models import LugarPriorizado,MetaMensualEP
from ..area_operativa.models import PlanArea,TipoOperativo
from ..eje_prevencion.models import PlanEje,EjeTrabajo,Producto,Subproducto
from ..delegacion.models import Usuario,Delegacion
from .filters import RespuestasEjeFilter,RespuestasAreaFilter


class RespuestasEPTemplateView(TemplateView):
    template_name='respuestas_eje.html'

    @method_decorator(login_required,csrf_exempt)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        page=request.GET.get('page',1)
        if self.request.user.is_superuser:
            ep_respuestas=EPRespuesta.objects.all()
        else:
            ep_respuestas=EPRespuesta.objects.filter(usuario=self.request.user)

        filtro=RespuestasEjeFilter(request.GET,queryset=ep_respuestas)
        respuestas=[]
        for respuesta in reversed(filtro.qs):
            respuestas.append(respuesta)
        try:
            paginator=Paginator(respuestas,5)
            respuestas= paginator.page(page)
        except Exception as e:
            print(e)
        return render(request,self.template_name,{'filtro':filtro,'paginator':paginator,'entity':respuestas})

class ActualizarEPTemplateView(TemplateView):
    template_name='update_eje.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,id=0):
        res=''
        lugares_priorizado=''
        planes=''
        ejes=''
        productos=''
        hay_registro=False
        if id>0:
            try:
                res=EPRespuesta.objects.get(pk=id)
                if res.usuario==self.request.user or self.request.user.is_superuser:
                    hay_registro=True
                    lugares_priorizado=LugarPriorizado.objects.filter(delegacion=self.request.user.delegacion)
                    planes=PlanEje.objects.all()
                    ejes=EjeTrabajo.objects.all()
                    productos=Producto.objects.all()
            except:
                hay_registro=False
        return render(request,self.template_name,{
                    'res':res,
                    'planes':planes,
                    'ejes':ejes,
                    'productos':productos,
                    'lugares_priorizado':lugares_priorizado,
                    'hay_registro':hay_registro
                })

class ResponderEPTemplateView(TemplateView):
    template_name='form_eje.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        lugares_priorizado=LugarPriorizado.objects.filter(delegacion=self.request.user.delegacion)
        meta=MetaMensualEP.objects.filter(delegacion=self.request.user.delegacion).last()
        hay_meta=False
        if meta:
            #if meta.asignado.month == datetime.now().month:
            hay_meta=True
        planes=PlanEje.objects.all()
        ejes=EjeTrabajo.objects.all()
        productos=Producto.objects.all()
        hay_datos=len(lugares_priorizado)>0 and len(planes)>0 and len(ejes)>0 and len(productos)>0 and hay_meta
        hay_datos=True
        return render(request,self.template_name,{
            'lugares_priorizado':lugares_priorizado,
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
        respuesta=''
        if id>0:
            try:
                respuesta=EPRespuesta.objects.get(pk=id)
                if respuesta.usuario==self.request.user or self.request.user.is_superuser:
                    hay_dato=True
                else:
                    hay_dato=False
            except:
                hay_dato=False
        return render(request,self.template_name,{
            'respuesta':respuesta,
            'hay_dato':hay_dato
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
        respuesta.respondido=now.strptime(jd['respondido'],'%Y-%m-%d')
        respuesta.latitud=jd['latitud']
        respuesta.longitud=jd['longitud']
        respuesta.delegacion=self.request.user.delegacion
        respuesta.usuario=self.request.user
        respuesta.lugar_priorizado=LugarPriorizado.objects.get(pk=jd['lugar_priorizado'])
        respuesta.lugar_no_priorizado=jd['lugar_no_priorizado']
        respuesta.cantidad=jd['cantidad']
        respuesta.lugar_especifico=jd['lugar_especifico']
        respuesta.plan=PlanEje.objects.get(pk=jd['plan'])
        respuesta.eje=EjeTrabajo.objects.get(pk=jd['eje'])
        eje=respuesta.eje
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
        respuesta._EJE=eje
        ingresado=respuesta.save()
        datos={'ingresado':ingresado}
        return JsonResponse(datos)

    def put(self,request):
        jd=json.loads(request.body)
        respuesta=EPRespuesta.objects.get(pk=jd['id'])
        eje=respuesta.eje
        respuesta.latitud=jd['latitud']
        respuesta.longitud=jd['longitud']
        respuesta.lugar_priorizado=LugarPriorizado.objects.get(pk=jd['lugar_priorizado'])
        respuesta.lugar_no_priorizado=jd['lugar_no_priorizado']
        respuesta.cantidad=jd['cantidad']
        respuesta.lugar_especifico=jd['lugar_especifico']
        respuesta.plan=PlanEje.objects.get(pk=jd['plan'])
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
        respuesta._EJE=eje
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
        page=request.GET.get('page',1)
        if self.request.user.is_superuser:
            ao_respuestas=AORespuesta.objects.all()
        else:
            ao_respuestas=AORespuesta.objects.filter(usuario=self.request.user)

        filtro=RespuestasAreaFilter(request.GET,queryset=ao_respuestas)
        respuestas=[]
        for respuesta in reversed(filtro.qs):
            respuestas.append(respuesta)
        try:
            paginator=Paginator(respuestas,5)
            respuestas= paginator.page(page)
        except Exception as e:
            print(e)
        return render(request,self.template_name,{'filtro':filtro,'paginator':paginator,'entity':respuestas})

class ResponderAOTemplateView(TemplateView):
    template_name='form_operativo.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        lugares_priorizado=LugarPriorizado.objects.filter(delegacion=self.request.user.delegacion)
        planes=PlanArea.objects.all()
        operativos=TipoOperativo.objects.all()
        hay_datos=len(lugares_priorizado)>0 and len(planes)>0 and len(operativos)>0
        return render(request,self.template_name,{
            'lugares_priorizado':lugares_priorizado,
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
        respuesta.delegacion=self.request.user.delegacion
        respuesta.usuario=self.request.user
        respuesta.lugar_priorizado=LugarPriorizado.objects.get(pk=jd['lugar_priorizado'])
        respuesta.lugar_no_priorizado=jd['lugar_no_priorizado']
        respuesta.cantidad=jd['cantidad']
        respuesta.lugar_apoyo=jd['lugar_apoyo']
        respuesta.plan=PlanArea.objects.get(pk=jd['plan'])
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
        respuesta.lugar_priorizado=LugarPriorizado.objects.get(pk=jd['lugar_priorizado'])
        respuesta.lugar_no_priorizado=jd['lugar_no_priorizado']
        respuesta.cantidad=jd['cantidad']
        respuesta.lugar_apoyo=jd['lugar_apoyo']
        respuesta.plan=PlanArea.objects.get(pk=jd['plan'])
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
        respuesta=''
        if id>0:
            try:
                respuesta=AORespuesta.objects.get(pk=id)
                if respuesta.usuario==self.request.user or self.request.user.is_superuser:
                    hay_dato=True
                else:
                    hay_dato=False
            except:
                hay_dato=False
        return render(request,self.template_name,{
            'respuesta':respuesta,
            'hay_dato':hay_dato
        })

class ActualizarAOTemplateView(TemplateView):
    template_name='update_operativo.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,id=0):
        lugares_priorizado=''
        res=''
        planes=''
        operativos=''
        hay_registro=False
        if id>0:
            try:
                res=AORespuesta.objects.get(pk=id)
                if res.usuario==self.request.user or self.request.user.is_superuser:
                    hay_registro=True
                    lugares_priorizado=LugarPriorizado.objects.filter(delegacion=self.request.user.delegacion)
                    planes=PlanArea.objects.all()
                    operativos=TipoOperativo.objects.all()
            except:
                hay_registro=False
        return render(request,self.template_name,{
            'res':res,
            'planes':planes,
            'operativos':operativos,
            'lugares_priorizado':lugares_priorizado,
            'hay_registro':hay_registro
        })