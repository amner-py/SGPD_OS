from django.shortcuts import render
from django.views.generic import TemplateView,UpdateView
from django.http.response import JsonResponse
from django.urls import reverse_lazy
from .models import SeccionInicio,ImgInicio,RedSocial
from ..delegacion.models import Usuario
from ..delegacion.forms import UsuarioChangeForm


def page_not_found404(request,exception):
    return render(request,'404.html')


class PerfilView(UpdateView):
    model=Usuario
    form_class=UsuarioChangeForm
    success_url=reverse_lazy('perfil')
    template_name='perfil.html'
    url_redirect=success_url
    
    '''def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action=request.POST['action']
            if action == 'edit':
                form=self.get_form()
                data=form.save()
            else:
                data['error']='No se ha ingresado'
        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Editar Usuario'
        context['entity']='Delegacion'
        context['list_url']=self.success_url
        context['action']='edit'
        return context'''

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
