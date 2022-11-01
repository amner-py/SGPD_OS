from django.views.generic import TemplateView
from django.shortcuts import render
from ..asignacion.models import Asignacion

class DepartamentoView(TemplateView):
    template_name='departamentos_view.html'


class DepaChiquimulaView(TemplateView):
    template_name='chiquimula/depa_chiquimula.html'

class ChiquiSanJoseLaAradaView(TemplateView):
    template_name='chiquimula/san_jose_la_arada.html'

class EsquipulasView(TemplateView):
    template_name='chiquimula/esquipulas.html'

    def get(self, request, *args, **kwargs):
        asignaciones = Asignacion.objects.all()
        
        hay_asignaciones = len(asignaciones)>0
        return render(request,self.template_name,{'asignaciones':asignaciones,'hay_asignaciones':hay_asignaciones})