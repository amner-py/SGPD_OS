from django.shortcuts import render
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Usuario
from .forms import PerfilUsuarioForm


class EditarPerfilView(UpdateView):
    model=Usuario
    form_class=PerfilUsuarioForm
    template_name='editar_perfil.html'
    success_url=reverse_lazy('inicio')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object=self.get_object
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user