from django.shortcuts import render
from django.views.defaults import page_not_found
from django.views.generic import TemplateView
from .models import SeccionInicio,ImgInicio,RedSocial


def get_error_404(request,*args,**kwargs):
    template_name = '404.html'
 
    return page_not_found(request, template_name=template_name)


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
