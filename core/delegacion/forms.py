from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Usuario

class UsuarioChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model=Usuario
        

class UsuarioCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=Usuario