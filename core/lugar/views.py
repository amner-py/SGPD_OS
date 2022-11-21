from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from ..asignacion.models import Asignacion
from .models import Departamento


class DepartamentoView(TemplateView):
    template_name='departamentos_view.html'
    
    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self,request):
        departamentos=Departamento.objects.all()
        hay_departamentos = len(departamentos)>0
        return render(request,self.template_name,{'departamentos':departamentos,'hay_departamentos':hay_departamentos})


class DepaChiquimulaView(TemplateView):
    template_name='chiquimula/depa_chiquimula.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

class ChiquiSanJoseLaAradaView(TemplateView):
    template_name='chiquimula/san_jose_la_arada.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

class EsquipulasView(TemplateView):
    template_name='chiquimula/esquipulas.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    
    def get(self, request, *args, **kwargs):
        asignaciones = Asignacion.objects.all()
        
        hay_asignaciones = len(asignaciones)>0
        return render(request,self.template_name,{'asignaciones':asignaciones,'hay_asignaciones':hay_asignaciones})