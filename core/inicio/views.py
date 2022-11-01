from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http.response import JsonResponse
from .models import SeccionInicio,ImgInicio,RedSocial

class InicioView(TemplateView):
    template_name='inicio.html'


    def get(self, request, *args, **kwargs):
        secciones = SeccionInicio.objects.all()
        imagenes = ImgInicio.objects.all()
        redes = RedSocial.objects.all()
        hay_redes = len(redes)>0
        hay_imagenes = len(imagenes)>0
        hay_secciones = len(secciones)>0
        return render(request,self.template_name,{'secciones':secciones,'hay_secciones':hay_secciones,'imagenes':imagenes,'hay_imagenes':hay_imagenes,'redes':redes,'hay_redes':hay_redes})


class SeccionView(View):
    
    def get(self,request):
        secciones=list(SeccionInicio.objects.values())
        if len(secciones)>0:
            datos={'message':'success','hay_seccion':True,'secciones':secciones}
        else:
            datos={'message':'wrong','hay_seccion':False}
        return JsonResponse(datos)
    
    
    def post(self,request):
        pass


    def put(self,request):
        pass


    def delete(self,request):
        pass