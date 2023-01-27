import django_filters as filters
from .models import EPRespuesta
from .forms import RespuestaFiltroForm
from ..delegacion.models import Delegacion
from ..eje_prevencion.models import PlanEje,EjeTrabajo,Producto,Subproducto
from ..area_operativa.models import PlanArea,TipoOperativo

class RespuestasEjeFilter(filters.FilterSet):
    respondido = filters.DateFromToRangeFilter()
    delegacion = filters.ModelChoiceFilter(queryset=Delegacion.objects.all())
    plan = filters.ModelChoiceFilter(queryset=PlanEje.objects.all())
    eje = filters.ModelChoiceFilter(queryset=EjeTrabajo.objects.all())
    producto = filters.ModelChoiceFilter(queryset=Producto.objects.all())
    subproducto = filters.ModelChoiceFilter(queryset=Subproducto.objects.all())

    class Meta:
        model= EPRespuesta
        fields=['respondido','delegacion','plan','eje','producto','subproducto']


class RespuestasAreaFilter(filters.FilterSet):
    respondido = filters.DateFromToRangeFilter()
    delegacion = filters.ModelChoiceFilter(queryset=Delegacion.objects.all())
    plan = filters.ModelChoiceFilter(queryset=PlanArea.objects.all())
    operativo = filters.ModelChoiceFilter(queryset=TipoOperativo.objects.all())

    class Meta:
        model= EPRespuesta
        fields=['respondido','delegacion','plan','operativo']