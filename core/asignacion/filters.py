import django_filters as filters
from .models import MetaMensualEP

class MetasEjeFilter(filters.FilterSet):
    asignado_year=filters.NumberFilter(lookup_expr='year')

    class Meta:
        model=MetaMensualEP
        fields=['asignado']